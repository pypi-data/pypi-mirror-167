from dataclasses import dataclass
from pymich.michelson_types import *
from pymich.stdlib import transaction


@dataclass(kw_only=True)
class Escrow(BaseContract):
    seller: Address
    buyer: Address
    price: Mutez
    paid: bool
    confirmed: bool

    def pay(self) -> None:
        if Tezos.sender != self.buyer:
            raise Exception("You are not the seller")

        if Tezos.amount != self.price:
            raise Exception("Not the right price")

        if self.paid:
            raise Exception("You have already paid!")

        self.paid = True

    def confirm(self) -> None:
        if Tezos.sender != self.buyer:
            raise Exception("You are not the buyer")

        if not self.paid:
            raise Exception("You have not paid")

        if self.confirmed:
            raise Exception("Already confirmed")

        self.confirmed = True

    def claim(self) -> None:
        if Tezos.sender != self.seller:
            raise Exception("You are not the seller")

        if not self.confirmed:
            raise Exception("Not confirmed")

        transaction(Contract[Unit](Tezos.sender), Tezos.balance, Unit())

