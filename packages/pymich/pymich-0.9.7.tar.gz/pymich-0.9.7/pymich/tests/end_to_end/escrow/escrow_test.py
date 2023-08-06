from pymich.test_utils import TestContract

import pathlib
import os

class TestContract(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "escrow.py")

    def test_pay(self):
        seller, buyer = self.make_n_test_accounts(2)
        price = 20

        init_storage = {
            'seller': seller,
            'buyer': buyer,
            'price': price,
            'paid': False,
            'confirmed': False,
        }

        new_storage = self.contract.pay().interpret(storage=init_storage, sender=buyer, amount=price).storage

        self.assertEqual(new_storage['paid'], True)

        with self.raisesMichelsonError('You have already paid!'):
            self.contract.pay().interpret(storage=new_storage, sender=buyer, amount=price).storage

        with self.raisesMichelsonError('Not the right price'):
            self.contract.pay().interpret(storage=init_storage, sender=buyer, amount=0).storage

        with self.raisesMichelsonError('You are not the seller'):
            self.contract.pay().interpret(storage=init_storage, sender=seller, amount=price).storage

    def test_confirm(self):
        seller, buyer = self.make_n_test_accounts(2)
        price = 20

        init_storage = {
            'seller': seller,
            'buyer': buyer,
            'price': price,
            'paid': True,
            'confirmed': False,
        }

        new_storage = self.contract.confirm().interpret(storage=init_storage, sender=buyer, amount=price).storage

        self.assertEqual(new_storage['confirmed'], True)

        with self.raisesMichelsonError('Already confirmed'):
            self.contract.confirm().interpret(storage=new_storage, sender=buyer, amount=price).storage

        with self.raisesMichelsonError('You are not the buyer'):
            self.contract.confirm().interpret(storage=init_storage, sender=seller, amount=price).storage

        init_storage['paid'] = False

        with self.raisesMichelsonError('You have not paid'):
            self.contract.confirm().interpret(storage=init_storage, sender=buyer, amount=price).storage

    def test_claim(self):
        seller, buyer = self.make_n_test_accounts(2)
        price = 20

        init_storage = {
            'seller': seller,
            'buyer': buyer,
            'price': price,
            'paid': True,
            'confirmed': True,
        }

        ops = self.contract.claim().interpret(storage=init_storage, sender=seller).operations

        self.assertEqual(len(ops), 1)
        self.assertEqual(ops[0]['destination'], seller)
        self.assertEqual(ops[0]['amount'], str(0))
