import unittest
from pymich.michelson_types import Nat, Address, BigMap, KeyType, ValueType, Tezos

admin = Address("tz3M4KAnKF2dCSjqfa1LdweNxBGQRqzvPL88")
investor = Address("KT1EwUrkbmGxjiRvmEAa8HLGhjJeRocqVTFi")

from pymich.tests.end_to_end.FA12.FA12 import FA12, AllowanceKey
from typing import Dict


def dict_to_big_map(d: Dict[KeyType, ValueType]) -> BigMap[KeyType, ValueType]:
    big_map = BigMap[KeyType, ValueType]()
    for key, value in d.items():
        big_map[key] = value
    return big_map


def FactoryFA12(owner: Address, tokens_dict: Dict[Address, Nat]) -> FA12:
    tokens = BigMap[Address, Nat]()
    total_supply = Nat(0)
    for address, amount in tokens_dict.items():
        tokens[address] = amount
        total_supply += amount
    return FA12(owner=owner, tokens=tokens, allowances=BigMap(), total_supply=total_supply)


class TestContract(unittest.TestCase):
    def test_mint(self) -> None:
        contract = FactoryFA12(admin, {})
        amount = Nat(10)
        Tezos.sender.address = admin.address
        contract.mint(admin, amount)

        assert contract.tokens[admin] == amount

        contract = FA12(owner=investor, tokens=BigMap(), allowances=BigMap(), total_supply=Nat(0))
        with self.assertRaises(Exception) as e:
            contract.mint(investor, amount)
        self.assertEqual(e.exception.args[0], 'Only owner can mint')

    def test_transfer(self) -> None:
        amount_1, amount_2 = Nat(10), Nat(4)
        contract = FactoryFA12(admin, {admin: amount_1})

        contract.transfer(admin, investor, amount_2)

        assert contract.tokens[admin] == abs(amount_1 - amount_2)
        assert contract.tokens[investor] == amount_2

        with self.assertRaises(Exception) as e:
            contract.transfer(admin, investor, Nat(100))
        self.assertEqual(e.exception.args[0], 'NotEnoughBalance')

    def todo_test_approve(self) -> None:
        # make dataclasses hashable by default by ignoring `unsafe_hash` in dataclass param in compiler)
        amount = Nat(10)
        contract = FactoryFA12(admin, {})
        contract.approve(investor, amount)
        breakpoint()
        assert contract.allowances[AllowanceKey(admin, investor)] == amount

if __name__ == "__main__":
    unittest.main()

from typing import NamedTuple

class ANamedTuple(NamedTuple):
    """a docstring"""
    foo: int
    bar: int
    baz: int

ANamedTuple(1, 2, 3)._replace(foo=2)
