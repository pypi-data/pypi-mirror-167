from pymich.test_utils import TestContract

import pathlib
import os


class TestContract(TestContract):
    contract_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "multi_asset.py")

    def test_create_token(self):
        storage = self.contract.storage.dummy()
        owner = self.make_test_account()
        storage["owner"] = owner
        new_storage = self.contract.create_token({"token_id": 1, "token_info": {"yo": bytes("hello my name is".encode("latin-1"))}}).interpret(storage=storage, sender=owner).storage
        self.assertEqual(new_storage["token_metadata"][1]["token_info"]["yo"], b"hello my name is")

        with self.raisesMichelsonError('FA2_DUP_TOKEN_ID'):
            self.contract.create_token({"token_id": 1, "token_info": {"yo": bytes("hello my name is".encode("latin-1"))}}).interpret(storage=new_storage, sender=owner).storage

    def test_mint(self):
        storage = self.contract.storage.dummy()
        owner = self.make_test_account()
        storage["owner"] = owner
        new_storage = self.contract.create_token({"token_id": 1, "token_info": {"yo": bytes("hello my name is".encode("latin-1"))}}).interpret(storage=storage, sender=owner).storage
        new_storage = self.contract.mint_tokens({"owner": owner, "token_id": 1, "amount": 10}).interpret(storage=new_storage, sender=owner).storage

        self.assertEqual(new_storage["token_total_supply"], {1: 10})
        self.assertEqual(new_storage["ledger"][(owner, 1)], 10)

    def test_mint_two_tokens(self):
        storage = self.contract.storage.dummy()
        owner = self.make_test_account()
        storage["owner"] = owner
        new_storage = self.contract.create_token({"token_id": 1, "token_info": {"yo": bytes("hello my name is".encode("latin-1"))}}).interpret(storage=storage, sender=owner).storage
        new_storage = self.contract.mint_tokens({"owner": owner, "token_id": 1, "amount": 10}).interpret(storage=new_storage, sender=owner).storage
        new_storage = self.contract.create_token({"token_id": 2, "token_info": {"yo": bytes("hello my name is".encode("latin-1"))}}).interpret(storage=new_storage, sender=owner).storage
        new_storage = self.contract.mint_tokens({"owner": owner, "token_id": 2, "amount": 10}).interpret(storage=new_storage, sender=owner).storage

    def test_transfer(self):
        storage = self.contract.storage.dummy()
        owner, investor = self.make_n_test_accounts(2)
        storage["owner"] = owner
        new_storage = self.contract.create_token({"token_id": 1, "token_info": {"yo": bytes("hello my name is".encode("latin-1"))}}).interpret(storage=storage, sender=owner).storage

        investor = "KT1EwUrkbmGxjiRvmEAa8HLGhjJeRocqVTFi"
        new_storage = self.contract.mint_tokens({"owner": owner, "token_id": 1, "amount": 10}).interpret(storage=new_storage, sender=owner).storage

        transfer_param = [
            {
                "from_": owner,
                "txs": [
                    {"amount": 4, "token_id": 1, "to_": investor},
                    {"amount": 4, "token_id": 1, "to_": investor},
                ]
            }
        ]
        new_storage = self.contract.transfer(transfer_param).interpret(storage=new_storage, sender=owner).storage

        self.assertEqual(new_storage["ledger"][(owner, 1)], 2)
        self.assertEqual(new_storage["ledger"][(investor, 1)], 8)

        new_storage["operators"] = {
            (investor, owner, 1): 0,
        }
        transfer_param = [
            {
                "from_": owner,
                "txs": [
                    {"amount": 1, "token_id": 1, "to_": investor},
                    {"amount": 1, "token_id": 1, "to_": investor},
                ]
            },
            {
                "from_": investor,
                "txs": [
                    {"amount": 2, "token_id": 1, "to_": owner},
                    {"amount": 2, "token_id": 1, "to_": owner},
                ]
            }
        ]
        new_storage = self.contract.transfer(transfer_param).interpret(storage=new_storage, sender=owner).storage
        self.assertEqual(new_storage["ledger"][(owner, 1)], 4)
        self.assertEqual(new_storage["ledger"][(investor, 1)], 6)

        new_storage = self.contract.create_token({"token_id": 2, "token_info": {"lo": bytes("slim shady".encode("latin-1"))}}).interpret(storage=new_storage, sender=owner).storage

        new_storage = self.contract.mint_tokens({"owner": owner, "token_id": 2, "amount": 10}).interpret(storage=new_storage, sender=owner).storage

        new_storage["operators"][(investor, owner, 2)] = 0

        transfer_param = [
            {
                "from_": owner,
                "txs": [
                    {"amount": 2, "token_id": 2, "to_": investor},
                    {"amount": 2, "token_id": 2, "to_": investor},
                ]
            },
            {
                "from_": investor,
                "txs": [
                    {"amount": 1, "token_id": 1, "to_": owner},
                    {"amount": 1, "token_id": 1, "to_": owner},
                ]
            }
        ]

        new_storage = self.contract.transfer(transfer_param).interpret(storage=new_storage, sender=owner).storage
