from pytezos.operation.result import OperationResult
from pymich.test_utils import TestContract

from pytezos import pytezos

import pathlib
import os


ALICE_KEY = "edsk3EQB2zJvvGrMKzkUxhgERsy6qdDDw19TQyFWkYNUmGSxXiYm7Q"
ALICE_PK = "tz1Yigc57GHQixFwDEVzj5N1znSCU3aq15td"
SHELL = "http://tzlocal:8732"
using_params = dict(shell=SHELL, key=ALICE_KEY)
pytezos = pytezos.using(**using_params)
send_conf = dict(min_confirmations=1)

bob_key = pytezos.key.generate(export=False)


class TestSandbox(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "A.py")

    def deploy_contract(self):
        init_storage = {
            "B": ALICE_PK,
            "C": ALICE_PK,
            "value": "",
            "admin": bob_key.public_key_hash(),
        }
        opg = self.contract.using(**using_params).originate(initial_storage=init_storage).send(**send_conf)
        addr = OperationResult.from_operation_group(opg.opg_result)[0].originated_contracts[0]
        contract_ci = pytezos.using(**using_params).contract(addr)

        return contract_ci

    def test_cross_contract_calls(self):
        A_ci = self.deploy_contract()
        B_ci = self.deploy_contract()
        C_ci = self.deploy_contract()
        D_ci = self.deploy_contract()

        A_ci.set_B(B_ci.address).send(**send_conf)
        A_ci.set_C(C_ci.address).send(**send_conf)

        B_ci.set_B(D_ci.address).send(**send_conf)

        C_ci.set_C(A_ci.address).send(**send_conf)

        A_ci.call_B_and_C({"value_b": "B", "value_c": "C"}).with_amount(1_000).send(**send_conf)

        assert int(pytezos.using(shell=SHELL, key=bob_key).account()["balance"]) == 1_000

        assert A_ci.storage["value"]() == "C"
        assert B_ci.storage["value"]() == ""
        assert C_ci.storage["value"]() == ""
        assert D_ci.storage["value"]() == "B"
