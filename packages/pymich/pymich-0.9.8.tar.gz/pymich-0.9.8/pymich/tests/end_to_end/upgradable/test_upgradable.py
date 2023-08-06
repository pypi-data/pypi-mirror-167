from pymich.test_utils import TestContract
from pytezos.michelson.format import micheline_to_michelson
from pytezos.contract.result import OperationResult

from pymich.compiler import Compiler

from pytezos import pytezos

import pathlib
import os


ALICE_KEY = "edsk3EQB2zJvvGrMKzkUxhgERsy6qdDDw19TQyFWkYNUmGSxXiYm7Q"
ALICE_PK = "tz1Yigc57GHQixFwDEVzj5N1znSCU3aq15td"
SHELL = "http://localhost:8732"
using_params = dict(shell=SHELL, key=ALICE_KEY)
pytezos = pytezos.using(**using_params)
send_conf = dict(min_confirmations=1)


def extract_function_body(lambda_micheline):
    return lambda_micheline[0]["args"][2]


double_source = f"""
def f(x: Nat) -> Nat:
    return x * Nat(2)
"""
triple_source = f"""
def f(x: Nat) -> Nat:
    return x * Nat(3)
"""

class TestContract(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "upgradable.py")

    def test_vm(self):
        double_micheline = Compiler(double_source).compile_expression()
        init_storage = self.contract.storage.dummy()
        init_storage["f"] = micheline_to_michelson(extract_function_body(double_micheline))
        new_storage = self.contract.update_counter(10).interpret(storage=init_storage).storage
        self.assertEqual(new_storage["counter"], 20)


    def skip_in_ci_for_now__test_deploy_sandbox(self):
        double_micheline = Compiler(double_source).compile_expression()
        init_storage = self.contract.storage.dummy()
        init_storage["f"] = micheline_to_michelson(extract_function_body(double_micheline))

        self.contract = self.contract.using(**using_params)
        opg = self.contract.originate(initial_storage=init_storage).send(**send_conf)
        addr = OperationResult.from_operation_group(opg.opg_result)[0].originated_contracts[0]
        ci = pytezos.using(**using_params).contract(addr)

        ci.update_counter(10).send(**send_conf)
        self.assertEqual(ci.storage["counter"](), 20)

        triple_micheline = Compiler(triple_source).compile_expression()
        triple = micheline_to_michelson(extract_function_body(triple_micheline))

        ci.update_f(triple).send(**send_conf)
        ci.update_counter(10).send(**send_conf)
        self.assertEqual(ci.storage["counter"](), 30)
