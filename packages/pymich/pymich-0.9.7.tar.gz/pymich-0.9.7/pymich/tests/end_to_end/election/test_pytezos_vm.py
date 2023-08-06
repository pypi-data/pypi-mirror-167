from pymich.test_utils import TestContract

import pathlib
import os

class TestContract(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "election.py")

    def test_open(self):
        init_storage = self.contract.storage.dummy()
        admin = self.make_test_account()
        init_storage['admin'] = admin

        new_storage = self.contract.open({"_open": "foo", "manifest_url": "bar", "manifest_hash": "baz"}).interpret(storage=init_storage, sender=admin).storage
        self.assertEqual(new_storage['_open'], "foo")
        self.assertEqual(new_storage['manifest_url'], "bar")
        self.assertEqual(new_storage['manifest_hash'], "baz")

        with self.raisesMichelsonError('Only admin can call this entrypoint'):
            new_storage = self.contract.open({"_open": "foo", "manifest_url": "bar", "manifest_hash": "baz"}).interpret(storage=init_storage)

    def test_close(self):
        init_storage = self.contract.storage.dummy()
        admin = self.make_test_account()
        init_storage['admin'] = admin

        new_storage = self.contract.close("foo").interpret(storage=init_storage, sender=admin).storage
        self.assertEqual(new_storage['_close'], "foo")

        with self.raisesMichelsonError('Only admin can call this entrypoint'):
            new_storage = self.contract.close("foo").interpret(storage=init_storage)

    def test_artifacts(self):
        init_storage = self.contract.storage.dummy()
        admin = self.make_test_account()
        init_storage['admin'] = admin

        new_storage = self.contract.artifacts({"artifacts_url": "url", "artifacts_hash": "hash"}).interpret(storage=init_storage, sender=admin).storage
        self.assertEqual(new_storage['artifacts_url'], "url")
        self.assertEqual(new_storage['artifacts_hash'], "hash")

        with self.raisesMichelsonError('Only admin can call this entrypoint'):
            new_storage = self.contract.close("foo").interpret(storage=init_storage)
