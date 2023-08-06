import pathlib
import os

from pymich.test_utils import TestContract


class TestContract(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "FA12.py")

    def test_mint(self):
        storage = self.contract.storage.dummy()
        owner = self.make_test_account()
        storage['owner'] = owner

        storage = self.contract.mint({"_to": owner, "value": 10}).interpret(storage=storage, sender=owner).storage
        self.assertEqual(storage['tokens'], {owner: 10})

        with self.raisesMichelsonError('Only owner can mint'):
            self.contract.mint({"_to": owner, "value": 10}).interpret(storage=storage).storage

    def test_getAllowance(self):
        storage = self.contract.storage.dummy()
        owner, investor = self.make_n_test_accounts(2)
        storage['owner'] = owner

        amount = 10
        initial_storage = {"owner": owner, "total_supply": amount, "tokens": {}, "allowances": {(owner, investor): amount}}
        res = self.contract.getAllowance({"owner": owner, "spender": investor, "contract_2": None}).callback_view(storage= initial_storage)
        self.assertEqual(res, 10)

        res = self.contract.getAllowance({"owner": owner, "spender": investor, "contract_2": None}).callback_view()
        self.assertEqual(res, 0)

    def test_getBalance(self):
        storage = self.contract.storage.dummy()
        owner, investor = self.make_n_test_accounts(2)
        storage['owner'] = owner

        amount = 10
        initial_storage = {"owner": owner, "total_supply": amount, "tokens": {investor: amount}, "allowances": {}}
        res = self.contract.getBalance({"owner": investor, "contract_1": None}).callback_view(storage= initial_storage)
        self.assertEqual(res, 10)

        res = self.contract.getBalance({"owner": owner, "contract_1": None}).callback_view()
        self.assertEqual(res, 0)

    def test_getTotalSupply(self):
        self.assertEqual(self.contract.getTotalSupply().callback_view(), 0)

    def test_transfer(self):
        storage = self.contract.storage.dummy()
        owner, investor = self.make_n_test_accounts(2)
        storage['owner'] = owner
        storage['tokens'] = {owner: 10}

        storage = self.contract.transfer({"_to": investor, "_from": owner, "value": 4}).interpret(storage=storage, sender=owner).storage
        self.assertEqual(storage['tokens'], {owner: 6, investor: 4})

        with self.raisesMichelsonError('NotEnoughBalance'):
            self.contract.transfer({"_from": owner, "_to": investor, "value": 10}).interpret(storage=storage, sender=owner).storage

        with self.raisesMichelsonError('NotEnoughAllowance'):
            self.contract.transfer({"_from": owner, "_to": investor, "value": 10}).interpret(storage=storage, sender=investor).storage

        storage["allowances"] = {(owner, investor): 10}
        storage = self.contract.transfer({"_from": owner, "_to": investor, "value": 2}).interpret(storage=storage, sender=investor).storage
        assert storage["tokens"][investor] == 6

        with self.raisesMichelsonError('NotEnoughBalance'):
            self.contract.transfer({"_from": owner, "_to": investor, "value": 8}).interpret(storage=storage, sender=investor).storage

    def test_approve(self):
        storage = self.contract.storage.dummy()
        owner, investor = self.make_n_test_accounts(2)
        storage['owner'] = owner

        storage = self.contract.approve({"spender": investor, "value": 4}).interpret(storage=storage, sender=owner).storage
        self.assertEqual(storage['allowances'], {(owner, investor): 4})
