import pathlib
import os

from pymich.test_utils import TestContract


class TestContract(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "heap.py")

    def test_mint(self):
        storage = self.contract.storage.dummy()

        storage = self.contract.add().interpret().storage

        self.assertEqual(storage['a'], 10)
