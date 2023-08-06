import ast
from pymich.frontend.three_address_encode import ThreeAddressEncode
import pymich.frontend.passes as p


def python_to_ir(source_ast, std_lib):
    factor_out_storage = p.FactorOutStorage()
    tuplify_function_arguments = p.TuplifyFunctionArguments(std_lib)

    frontend_passes = [
        p.RewriteOperations(),
        p.RewriteViews(),
        factor_out_storage,
        p.RemoveSelfArgFromMethods(),
        p.AssignAllFunctionCalls(),
        p.HandleNoArgEntrypoints(),
        tuplify_function_arguments,
        ThreeAddressEncode(),
    ]

    new_ast = source_ast
    for frontend_pass in frontend_passes:
        new_ast = frontend_pass.visit(new_ast)
        new_ast = ast.fix_missing_locations(new_ast)

    new_ast.body = tuplify_function_arguments.dataclasses + new_ast.body
    if hasattr(factor_out_storage, "storage_dataclass"):
        new_ast = p.PlaceBackStorageDataclass(
            factor_out_storage.storage_dataclass
        ).visit(new_ast)

    new_ast = ast.fix_missing_locations(new_ast)
    return new_ast
