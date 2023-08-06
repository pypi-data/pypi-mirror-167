from datetime import datetime
from pymich.test_utils import TestContract

import pathlib
import os


class TestContract(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "visitor.py")
    now = int(datetime.timestamp(datetime.now()))

    def test_register(self):
        init_storage = {'total_visits': 0, 'visitors': {}}

        user = self.make_test_account()
        new_storage = self.contract.register("Dogus").interpret(storage=init_storage, sender=user, now=self.now).storage

        self.assertEqual(new_storage['visitors'][user], {'visits': 0, 'name': 'Dogus', 'last_visit': self.now})
        self.assertEqual(new_storage['total_visits'], 0)

    def test_visit(self):
        user_1, user_2 = self.make_n_test_accounts(2)
        init_storage = {'total_visits': 0, 'visitors': {user_1: {'visits': 0, 'name': 'Dogus', 'last_visit': self.now}}}

        new_storage = self.contract.visit().interpret(storage=init_storage, sender=user_1, amount=5, now=self.now + 10 * 24 * 60 * 60).storage

        self.assertEqual(new_storage['visitors'][user_1]['visits'], 1)
        self.assertEqual(new_storage['total_visits'], 1)

        with self.raisesMichelsonError('You need to wait 10 days between visits'):
            self.contract.visit().interpret(storage=init_storage, sender=user_1, amount=5, now=self.now).storage

        with self.raisesMichelsonError('You need to pay 5 mutez on your first visit!'):
            self.contract.visit().interpret(storage=init_storage, sender=user_1, amount=0, now=self.now + 10 * 24 * 60 * 60).storage

        init_storage['visitors'][user_1]['visits'] = 1

        with self.raisesMichelsonError('You need to pay 3 mutez to visit!'):
            self.contract.visit().interpret(storage=init_storage, sender=user_1, amount=0, now=self.now + 10 * 24 * 60 * 60).storage

        with self.raisesMichelsonError('You are not registered yet!'):
            self.contract.visit().interpret(storage=init_storage, sender=user_2).storage
