from pymich.test_utils import TestContract

import pathlib
import os


class TestContractNew(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "auction.py")

    def test_register(self):
        admin, investor = self.make_n_test_accounts(2)

        init_storage = {'owner': admin, 'top_bidder': admin, 'bids': {admin: 0}}

        amount = 10
        new_storage = self.contract.bid().interpret(storage=init_storage, sender=investor, amount=amount).storage

        self.assertEqual(new_storage['top_bidder'], investor)
        self.assertEqual(new_storage['bids'][investor], amount)

        with self.raisesMichelsonError('You have already made a bid'):
            self.vm.contract.bid().interpret(storage=new_storage, sender=investor)

    def test_collect_top_bid(self):
        admin, investor = self.make_n_test_accounts(2)

        amount = 10
        init_storage = {'owner': admin, 'top_bidder': investor, 'bids': {investor: amount}}

        ops = self.contract.collectTopBid().interpret(storage=init_storage, sender=admin).operations

        self.assertEqual(len(ops), 1)
        self.assertEqual(ops[0]['destination'], admin)
        self.assertEqual(ops[0]['amount'], str(amount))

        with self.raisesMichelsonError('Only the owner can collect the top bid'):
            self.contract.collectTopBid().interpret(storage=init_storage, sender=investor)

    def test_claim(self):
        admin, investor_1, investor_2 = self.make_n_test_accounts(3)
        amount_1, amount_2 = 10, 5
        init_storage = {'owner': admin, 'top_bidder': investor_1, 'bids': {investor_1: amount_1, investor_2: amount_2}}

        ops = self.contract.claim().interpret(storage=init_storage, sender=investor_2).operations

        self.assertEqual(len(ops), 1)
        self.assertEqual(ops[0]['destination'], investor_2)
        self.assertEqual(ops[0]['amount'], str(amount_2))

        with self.raisesMichelsonError('You have not made any bids!'):
            self.contract.claim().interpret(storage=init_storage, sender=admin).operations

        with self.raisesMichelsonError('You won!'):
            self.contract.claim().interpret(storage=init_storage, sender=investor_1).operations
