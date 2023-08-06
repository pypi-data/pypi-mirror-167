import copy
from dataclasses import dataclass
from typing import Any, Dict, List

import pymich.middle_end.ir.instr_types as t
from pymich.utils.helpers import Tree
import pymich.utils.exceptions as E


@dataclass
class Instr:
    name: str
    args: List[Any]
    kwargs: Dict[str, Any]

    def assert_n_args(self, n: int, error_message: str):
        if len(self.args) != n:
            raise E.InvalidMichelsonException(error_message)

    def assert_min_args(self, n: int, error_message: str):
        if len(self.args) < n:
            raise E.InvalidMichelsonException(error_message)

    def assert_arg_type(self, n: int, type_, error_message: str):
        self.assert_min_args(n, error_message)
        if not isinstance(self.args[n], type_):
            raise E.InvalidMichelsonException(error_message)

    def __str__(self):
        args = ""
        for arg in self.args:
            args += str(arg) + " "
        return f"{self.name} {args}"


@dataclass
class Entrypoint:
    prototype: t.FunctionPrototype
    instructions: List[Instr]


class ParameterTree(Tree):
    def make_node(self, left, right):
        return t.Or(left, right)

    def get_left(self, tree_node):
        return tree_node.left_type

    def get_right(self, tree_node):
        return tree_node.right_type

    def set_right(self, tree_node, value):
        tree_node.right_type = value


class EntrypointTree(Tree):
    def make_node(self, left=None, right=None):
        if not left:
            left = []
        if not right:
            right = []
        return Instr("IF_LEFT", [left, right], {})

    def get_left(self, tree_node):
        return tree_node.args[0]

    def get_right(self, tree_node):
        return tree_node.args[1]

    def set_right(self, tree_node, value):
        tree_node.args[1] = value

    def get_leaf_from_element(self, element):
        return element.instructions

    def format_leaf(self, leaf):
        return leaf if type(leaf) == list else [leaf]


@dataclass
class Contract:
    storage: Any
    storage_type: t.Type
    entrypoints: Dict[str, Entrypoint]
    instructions: List[Instr]

    def add_entrypoint(self, name: str, entrypoint: Entrypoint):
        self.entrypoints[name] = entrypoint

    def get_storage_type(self):
        return self.storage_type

    def get_parameter_type(self):
        entrypoint_names = self.entrypoints.keys()
        if len(entrypoint_names) == 1:
            entrypoint_name = list(entrypoint_names)[0]
            return self.entrypoints[entrypoint_name].prototype.arg_type
        else:
            parameter_tree = ParameterTree()
            entrypoints = [
                self.entrypoints[name].prototype.arg_type
                for name in sorted(entrypoint_names)
            ]

            for i, entrypoint in enumerate(entrypoints):
                if type(entrypoint) == t.Record:
                    # we do not want to override the record annotation for all record
                    # calls but want to annotate them with the entrypoint name, so we
                    # copy it and set the annotation then
                    entrypoints[i] = copy.deepcopy(entrypoint)
                    entrypoints[i].annotation = "%" + sorted(list(entrypoint_names))[i]
                else:
                    entrypoint.annotation = "%" + sorted(list(entrypoint_names))[i]

            return parameter_tree.list_to_tree(entrypoints)

    def get_contract_body(self):
        entrypoints = [
            self.entrypoints[name] for name in sorted(self.entrypoints.keys())
        ]
        entrypoint_tree = EntrypointTree()
        return entrypoint_tree.list_to_tree(entrypoints)
