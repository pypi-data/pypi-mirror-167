from dataclasses import dataclass
from pymich.michelson_types import *


@dataclass
class VisitorInfo(Record):
    visits: Nat
    name: String
    last_visit: Timestamp


@dataclass(kw_only=True)
class Visitor(BaseContract):
    visitors: BigMap[Address, VisitorInfo]
    total_visits: Nat

    def register(self, name: String) -> None:
        self.visitors[Tezos.sender] = VisitorInfo(Nat(0), name, Timestamp.now())

    def visit(self) -> None:
        if not (Tezos.sender in self.visitors):
            raise Exception("You are not registered yet!")

        n_visits = self.visitors[Tezos.sender].visits

        if Timestamp.now() - self.visitors[Tezos.sender].last_visit < Int(10) * Int(24) * Int(3600):
            raise Exception("You need to wait 10 days between visits")

        if n_visits == Nat(0) and Tezos.amount != Mutez(5):
            raise Exception("You need to pay 5 mutez on your first visit!")

        if n_visits != Nat(0) and Tezos.amount != Mutez(3):
            raise Exception("You need to pay 3 mutez to visit!")

        self.visitors[Tezos.sender].visits = n_visits + Nat(1)
        self.total_visits = self.total_visits + Nat(1)
