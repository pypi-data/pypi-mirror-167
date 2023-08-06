from pymich.compiler import Compiler
from pymich.test_utils import TestContract, VM

from pytezos.crypto.key import blake2b_32

import pathlib
import os

def hash_value(value: int):
    vm = VM()
    source = f"Bytes(Nat({value})).blake2b()"
    micheline = Compiler(source).compile_expression()
    vm.execute(micheline)
    return vm.stack.peek().value



class TestContract(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "lottery.py")

    def test_bet(self):
        alice, bob = self.make_n_test_accounts(2)

        init_storage = {
            "bid_amount": 10,
            "deadline_bet": 10000,
            "deadline_reveal": 20000,
            "bids": {},
            "nb_bids": 0,
            "nb_revealed": 0,
            "sum_values": 0,
        }

        bob_value = 10
        bob_hash = blake2b_32(str(bob_value)).digest()
        alice_value = 15
        alice_hash = blake2b_32(str(alice_value)).digest()

        new_storage = self.contract.bet(alice_hash).interpret(storage=init_storage, sender=alice, amount=10).storage


        self.assertEqual(new_storage['bids'][alice], {"value_hash": alice_hash, "num_bid": 0})
        self.assertEqual(new_storage['nb_bids'], 1)

        with self.raisesMichelsonError('You have not bidded the right amount'):
            self.contract.bet(alice_hash).interpret(storage=init_storage, sender=alice, amount=5).storage

    def test_reveal(self):
        alice = self.make_test_account()

        alice_value = 15
        alice_hash = hash_value(alice_value)

        init_storage = {
            "bid_amount": 10,
            "deadline_bet": 10000,
            "deadline_reveal": 20000,
            "bids": {
                alice: {
                    "value_hash": alice_hash,
                    "num_bid": 1,
                }
            },
            "nb_bids": 0,
            "nb_revealed": 0,
            "sum_values": 0,
        }

        new_storage = self.contract.reveal(alice_value).interpret(storage=init_storage, sender=alice).storage
        self.assertEqual(new_storage['sum_values'], alice_value)
        self.assertEqual(new_storage['nb_revealed'], 1)

        with self.raisesMichelsonError('Wrong hash'):
            self.contract.reveal(alice_value + 10).interpret(storage=init_storage, sender=alice).storage

    def test_claim(self):
        alice, bob = self.make_n_test_accounts(2)

        alice_value = 15
        alice_hash = hash_value(alice_value)
        bob_value = 10
        bob_hash = hash_value(bob_value)

        init_storage = {
            "bid_amount": 10,
            "deadline_bet": 10000,
            "deadline_reveal": 20000,
            "bids": {
                alice: {
                    "value_hash": alice_hash,
                    "num_bid": 0,
                },
                bob: {
                    "value_hash": bob_hash,
                    "num_bid": 1,
                }
            },
            "nb_bids": 0,
            "nb_revealed": 2,
            "sum_values": alice_value + bob_value,
        }

        ops = self.contract.claim().interpret(storage=init_storage, sender=bob, now=1000000, balance=20).operations
        self.assertEqual(ops[0]["destination"], bob)
        self.assertEqual(ops[0]["amount"], "20")

        with self.raisesMichelsonError('You have not won'):
            self.contract.claim().interpret(storage=init_storage, sender=alice, now=1000000, balance=20).storage
