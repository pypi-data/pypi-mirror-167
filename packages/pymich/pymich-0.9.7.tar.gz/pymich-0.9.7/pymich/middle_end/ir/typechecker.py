import ast

from pymich.middle_end.ir.instr_types import StdlibFunctionSpec, StdLibClassSpec
from pymich.utils.compiler_stdlib import StdLib
import pymich.middle_end.ir.instr_types as t
from pymich.utils.environment import Env
import pymich.utils.exceptions as E


class TypeChecker:
    def __init__(
        self, std_lib: StdLib | None = None, type_parser: t.TypeParser | None = None
    ) -> None:
        self.std_lib = std_lib if std_lib else StdLib()
        self.type_parser = type_parser if type_parser else t.TypeParser()

    def get_name_type(self, node, e: Env):
        if node.id in e.types:
            return e.types[node.id]
        elif node.id in self.std_lib.constants_mapping:
            if type(self.std_lib.constants_mapping[node.id]) == t.StdlibVariable:
                return self.std_lib.constants_mapping[node.id].type

            return self.std_lib.constants_mapping[node.id]
        else:
            raise E.FunctionNameException(node.id, node.lineno)

    def get_list_type(self, node, e: Env):
        if len(node.elts):
            elt_type = self.get_expression_type(node.elts[0], e)
            return t.List(elt_type)
        else:
            return t.List(t.Unknown())

    def get_dict_type(self, node, e: Env):
        if len(node.keys):
            key_type = self.get_expression_type(node.keys[0], e)
            value_type = self.get_expression_type(node.values[0], e)
            return t.Dict(key_type, value_type)
        else:
            return t.Dict(t.Unknown(), t.Unknown())

    def get_constant_type(self, node, e: Env):
        if type(node.value) == str:
            return t.PythonString()
        elif type(node.value) == int:
            return t.PythonInt()
        elif type(node.value) == bool:
            return t.Bool()
        else:
            raise E.TypeException(["str", "int", "bool"], node.value, node.lino)

    def get_subscript_type(self, node, e: Env):
        parent_type = self.get_expression_type(node.value, e)
        if type(parent_type) == t.Dict or type(parent_type) == t.BigMap:
            return parent_type.value_type
        elif type(parent_type) == t.List:
            return parent_type.element_type
        elif type(parent_type) == StdLibClassSpec:
            cast_type = self.type_parser.parse(node.slice, e)
            return parent_type.constructor.get_prototype([cast_type]).return_type
        elif type(parent_type) == StdlibFunctionSpec:
            cast_type = self.type_parser.parse(node.slice, e)
            return parent_type.get_prototype([cast_type]).return_type
        else:
            raise E.TypeException(t.polymorphic_types, parent_type, e)

    def get_attribute_type(self, node, e: Env):
        record = self.get_expression_type(node.value, e)
        if type(record) == StdLibClassSpec:
            if type(node.value) == ast.Name:
                if record.constructor:
                    record = record.constructor.get_prototype(t.Unknown()).return_type
                else:
                    if node.attr in record.attributes:
                        return record.attributes[node.attr].type
            elif type(record.value) == ast.Call:
                arg_types = [self.get_expression_type(arg, e) for arg in node.args]
                record = record.constructor.get_prototype(arg_types).return_type

        attr_value_type = type(record)
        if attr_value_type in self.std_lib.types_mapping:
            if node.attr in self.std_lib.types_mapping[attr_value_type].methods:
                method = self.std_lib.types_mapping[attr_value_type].methods[node.attr]
                return t.StdlibMethodInstance(
                    "",
                    method.get_prototype(record),
                    method.compile_callback,
                )
            else:
                raise E.CompilerException(
                    f"{node.attr} is not a method of type: {record}", node.lineno
                )

        if node.attr in record.attribute_names:
            return record.get_attribute_type(node.attr)
        else:
            raise E.AttributeException(record, node.attr, node.lineno)

    def get_call_type(self, node, e: Env):
        if type(node.func) == ast.Name and node.func.id in e.types:
            prototype = e.types[node.func.id]
            if type(prototype) == t.Record:
                # Dataclass constructor call
                return prototype
            elif isinstance(
                prototype, (t.StdlibMethodInstance, t.StdlibStaticMethodInstance)
            ):
                # Stdlib method call
                return prototype.signature.return_type
            elif isinstance(prototype, t.FunctionPrototype):
                if len(node.args) != 1:
                    raise E.CompilerException(
                        "Only uniary functions are supported at the IR level",
                        node.lineno,
                    )

                actual_type = self.get_expression_type(node.args[0], e)
                expected_type = prototype.arg_type
                if actual_type != expected_type:
                    raise E.FunctionParameterTypeException(
                        expected_type, actual_type, node.lineno
                    )
                return prototype.return_type
        elif (
            type(node.func) == ast.Name
            and node.func.id in self.std_lib.constants_mapping
        ):
            if type(self.std_lib.constants_mapping[node.func.id]) == StdlibFunctionSpec:
                return (
                    self.std_lib.constants_mapping[node.func.id]
                    .get_prototype()
                    .return_type
                )
            elif type(self.std_lib.constants_mapping[node.func.id]) == StdLibClassSpec:
                arg_types = [self.get_expression_type(arg, e) for arg in node.args]
                prototype = self.std_lib.constants_mapping[
                    node.func.id
                ].constructor.get_prototype(arg_types)
                if isinstance(prototype, t.MultiArgFunctionPrototype):
                    is_polymorphic = isinstance(prototype.arg_types[0], t.Unknown)
                    if arg_types != prototype.arg_types and not is_polymorphic:
                        raise E.TypeException(prototype.arg_types, arg_types, e)
                return prototype.return_type
            else:
                raise E.CompilerException(
                    f"Stdlib expression {node.func.id} cannot be typed", node.lineno
                )
        elif type(node.func) == ast.Attribute and node.func.attr == "unpack":
            if len(node.args) != 1:
                raise E.FunctionParameterTypeException("[Type]", node.args, node.lineno)
            cast_to_type = self.type_parser.parse(node.args[0], e)
            return (
                self.std_lib.types_mapping[t.Bytes]
                .methods["unpack"]
                .get_prototype(cast_to_type)
                .return_type
            )
        else:
            fun_type = self.get_expression_type(node.func, e)
            if isinstance(fun_type, t.StdlibMethodInstance):
                is_error = False

                if len(node.args) != len(fun_type.signature.arg_types):
                    is_error = True
                else:
                    for arg, expected_type in zip(
                        node.args, fun_type.signature.arg_types
                    ):
                        actual_type = self.type_parser.parse(arg, e)
                        if actual_type != expected_type:
                            is_error = True

                if is_error:
                    raise E.FunctionParameterTypeException(
                        fun_type.signature.arg_types, node.args, node.lineno
                    )

                return fun_type.signature.return_type
            else:
                return fun_type

    def get_compare_type(self, node, e: Env):
        return t.Bool()

    def get_binop_type(self, node, e: Env):
        allowed_operand_types = {
            ast.Sub: {
                (t.Nat(), t.Nat()): t.Int(),
                (t.Int(), t.Int()): t.Int(),
                (t.Nat(), t.Int()): t.Int(),
                (t.Int(), t.Nat()): t.Int(),
                (t.Mutez(), t.Mutez()): t.Option(t.Mutez()),
                (t.Datetime(), t.Int()): t.Datetime(),
                (t.Datetime(), t.Datetime()): t.Datetime(),
            },
            ast.Add: {
                (t.Nat(), t.Nat()): t.Nat(),
                (t.Int(), t.Int()): t.Int(),
                (t.Nat(), t.Int()): t.Int(),
                (t.Int(), t.Nat()): t.Int(),
                (t.Mutez(), t.Mutez()): t.Mutez(),
                (t.Datetime(), t.Int()): t.Datetime(),
                (t.Int(), t.Datetime()): t.Datetime(),
            },
            ast.Mult: {
                (t.Nat(), t.Nat()): t.Nat(),
                (t.Int(), t.Int()): t.Int(),
                (t.Nat(), t.Int()): t.Int(),
                (t.Int(), t.Nat()): t.Int(),
                (t.Mutez(), t.Nat()): t.Mutez(),
                (t.Nat(), t.Mutez()): t.Mutez(),
            },
            ast.FloorDiv: {
                (t.Nat(), t.Nat()): t.Nat(),
                (t.Int(), t.Int()): t.Int(),
                (t.Nat(), t.Int()): t.Int(),
                (t.Int(), t.Nat()): t.Int(),
                (t.Mutez(), t.Nat()): t.Mutez(),
                (t.Mutez(), t.Mutez()): t.Nat(),
            },
            ast.Mod: {
                (t.Nat(), t.Nat()): t.Nat(),
                (t.Int(), t.Int()): t.Int(),
                (t.Nat(), t.Int()): t.Int(),
                (t.Int(), t.Nat()): t.Int(),
                (t.Mutez(), t.Nat()): t.Mutez(),
                (t.Mutez(), t.Mutez()): t.Mutez(),
            },
        }

        op_type = type(node.op)
        if op_type not in allowed_operand_types:
            raise E.CompilerException(
                f"Unsupported operand ({node.op}, only [+, -, *, %, //] are supported)",
                node.lineno,
            )

        left_type = self.get_expression_type(node.left, e)
        right_type = self.get_expression_type(node.right, e)

        if (left_type, right_type) not in allowed_operand_types[op_type]:
            raise E.CompilerException(
                f"Unsupported types for operand {node.op}: [{left_type}, {right_type}]",
                node.lineno,
            )

        return allowed_operand_types[op_type][(left_type, right_type)]

    def get_expression_type(self, node, e: Env | None = None) -> t.Type:
        if not e:
            e = Env({}, -1, {}, {})
            self.e = e

        if type(node) == ast.Name:
            return self.get_name_type(node, e)
        elif type(node) == ast.List:
            return self.get_list_type(node, e)
        elif type(node) == ast.Dict:
            return self.get_dict_type(node, e)
        elif type(node) == ast.Constant:
            return self.get_constant_type(node, e)
        elif type(node) == ast.Subscript:
            return self.get_subscript_type(node, e)
        elif type(node) == ast.Attribute:
            return self.get_attribute_type(node, e)
        elif type(node) == ast.Call:
            return self.get_call_type(node, e)
        elif type(node) == ast.BinOp:
            return self.get_binop_type(node, e)
        elif type(node) == ast.BoolOp:
            return t.Bool()
        elif type(node) == ast.UnaryOp:
            if isinstance(node.op, (ast.USub, ast.UAdd)):
                operand_type = self.get_expression_type(node.operand, e)
                if not isinstance(operand_type, t.PythonInt):
                    raise E.TypeException(["python_int"], operand_type, node.lineno)
                return operand_type
            return t.Bool()
        elif type(node) == ast.Compare:
            return self.get_compare_type(node, e)
        else:
            raise E.CompilerException(f"Expression {node} cannot be typed", node.lineno)

    def typecheck_module(self, m: ast.Module, e: Env) -> None:
        for key, value in ast.iter_fields(m):
            if key == "body":
                for child_node in value:
                    self.typecheck_ir(child_node, e)

    def typecheck_ir(self, node_ast, e: Env | None = None):
        if not e:
            e = Env({}, -1, {}, {})
            self.e = e

        if type(node_ast) == ast.Module:
            self.typecheck_module(node_ast, e)
        elif type(node_ast) == ast.Expr:
            self.typecheck_module(node_ast.value, e)
        else:
            self.get_expression_type(node_ast, e)
