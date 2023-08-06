from dataclasses import dataclass
from pymich.michelson_types import *


@dataclass(eq=True, frozen=True)
class AllowanceKey(Record):
    owner: Address
    spender: Address


@dataclass(kw_only=True)
class FA12(BaseContract):
    tokens: BigMap[Address, Nat]
    allowances: BigMap[AllowanceKey, Nat]
    total_supply: Nat
    owner: Address

    def mint(self, _to: Address, value: Nat) -> None:
        if Tezos.sender != self.owner:
            raise Exception("Only owner can mint")

        self.total_supply = self.total_supply + value

        self.tokens[_to] = self.tokens.get(_to, Nat(0)) + value

    def approve(self, spender: Address, value: Nat) -> None:
        allowance_key = AllowanceKey(Tezos.sender, spender)

        previous_value = self.allowances.get(allowance_key, Nat(0))

        if previous_value > Nat(0) and value > Nat(0):
            raise Exception("UnsafeAllowanceChange")

        self.allowances[allowance_key] = value

    def transfer(self, _from: Address, _to: Address, value: Nat) -> None:
        if Tezos.sender != _from:
            allowance_key = AllowanceKey(_from, Tezos.sender)

            authorized_value = self.allowances.get(allowance_key, Nat(0))

            if (authorized_value - value) < Int(0):
                raise Exception("NotEnoughAllowance")

            self.allowances[allowance_key] = abs(authorized_value - value)

        from_balance = self.tokens.get(_from, Nat(0))

        if (from_balance - value) < Int(0):
            raise Exception("NotEnoughBalance")

        self.tokens[_from] = abs(from_balance - value)

        to_balance = self.tokens.get(_to, Nat(0))

        self.tokens[_to] = to_balance + value

    def getAllowance(self, owner: Address, spender: Address) -> Nat:
        return self.allowances.get(AllowanceKey(owner, spender), Nat(0))

    def getBalance(self, owner: Address) -> Nat:
        return self.tokens.get(owner, Nat(0))

    def getTotalSupply(self) -> Nat:
        return self.total_supply

