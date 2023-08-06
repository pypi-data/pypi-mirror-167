from dataclasses import dataclass

from pymich.michelson_types import *
from pymich.stdlib import *


@dataclass
class BidInfo(Record):
    value_hash: Bytes
    num_bid: Nat


@dataclass(kw_only=True)
class Lottery(BaseContract):
    bid_amount: Mutez
    deadline_bet: Timestamp
    deadline_reveal: Timestamp
    bids: BigMap[Address, BidInfo]
    nb_bids: Nat
    nb_revealed: Nat
    sum_values: Nat

    def bet(self, value_hash: Bytes) -> None:
        if Tezos.sender in self.bids:
            raise Exception("You have already made a bid")

        if Tezos.amount != self.bid_amount:
            raise Exception("You have not bidded the right amount")

        if Timestamp.now() > self.deadline_bet:
            raise Exception("Too late to make a bid")

        self.bids[Tezos.sender] = BidInfo(value_hash, self.nb_bids)
        self.nb_bids = self.nb_bids + Nat(1)

    def reveal(self, value: Nat) -> None:
        if not (Tezos.sender in self.bids):
            raise Exception("You have not made a bid")

        if Timestamp.now() > self.deadline_bet or Timestamp.now() > self.deadline_reveal:
            raise Exception("Too late to make a reveal")

        if Bytes(value).blake2b() != self.bids[Tezos.sender].value_hash:
            raise Exception("Wrong hash")

        self.sum_values = self.sum_values + value
        self.nb_revealed = self.nb_revealed + Nat(1)

    def claim(self) -> None:
        if Timestamp.now() < self.deadline_reveal:
            raise Exception("The lottery is not over")

        if not (Tezos.sender in self.bids):
            raise Exception("You have not made a bid")

        num_winner = self.sum_values % self.nb_revealed

        if self.bids[Tezos.sender].num_bid != num_winner:
            raise Exception("You have not won")

        transaction(Contract[Unit](Tezos.sender), Tezos.balance, Unit())
