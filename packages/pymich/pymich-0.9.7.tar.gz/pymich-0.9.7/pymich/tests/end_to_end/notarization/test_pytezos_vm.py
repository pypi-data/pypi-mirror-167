import pathlib
import os
import uuid

from hashlib import sha256

from pymich.michelson_types import *
from pymich.test_utils import TestContract

from pytezos import pytezos
from pytezos.contract.result import OperationResult

from pymich.tests.end_to_end.notarization.notarization import Notarization, DocumentId


ALICE_KEY = "edsk3EQB2zJvvGrMKzkUxhgERsy6qdDDw19TQyFWkYNUmGSxXiYm7Q"
ALICE_PK = "tz1Yigc57GHQixFwDEVzj5N1znSCU3aq15td"
SHELL = "http://tzlocal:8732"

using_params = dict(shell=SHELL, key=ALICE_KEY)
pytezos = pytezos.using(**using_params)
send_conf = dict(min_confirmations=1)


class TestPython(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "notarization.py")

    def test_add_document(self):
        doc_owner = Address("tzentity")
        notarization = Notarization(
            admin="tzadmin",
            document_hashes=BigMap[DocumentId, Bytes]()
        )
        Tezos.sender = doc_owner
        document_hash = Bytes(String("my_hash"))
        document_uuid = String("my_uuid")
        notarization.add_document(document_uuid, document_hash)
        doc_id, doc_id_value = [
            (k, v)
            for k, v in notarization.document_hashes._BigMap__dictionary.items()
        ][0]
        assert doc_id.owner == doc_owner
        assert doc_id.uuid == document_uuid
        assert doc_id_value == document_hash


class TestSandbox(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "notarization.py")

    def test_in_ci_for_now__test_deploy_sandbox(self):
        init_storage = self.contract.storage.dummy()

        self.contract = self.contract.using(**using_params)
        opg = self.contract.originate(initial_storage=init_storage).send(**send_conf)
        addr = OperationResult.from_operation_group(opg.opg_result)[0].originated_contracts[0]
        ci = pytezos.using(**using_params).contract(addr)

        doc_uuid = str(uuid.uuid4())
        doc_hash = sha256(doc_uuid.encode()).hexdigest().encode()
        ci.add_document({
            "document_uuid": doc_uuid,
            "document_hash": doc_hash,
        }).send(**send_conf)

        assert ci.storage["document_hashes"][{"owner": ALICE_PK, "uuid": doc_uuid}]() == doc_hash
