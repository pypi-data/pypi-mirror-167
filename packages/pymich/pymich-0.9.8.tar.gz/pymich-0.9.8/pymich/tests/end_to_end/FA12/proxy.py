from dataclasses import dataclass
from pymich.michelson_types import *
from pymich.stdlib import *


@dataclass
class TransferParam(Record):
    _from: Address
    _to: Address
    value: Nat

class Proxy(Contract):
    admin: Address
    fa12: Address

    def proxy_transfer(self) -> None:
        transfer_entrypoint = Contract[TransferParam](self.fa12, "%transfer")

        transaction(
            transfer_entrypoint,
            Mutez(0),
            TransferParam(self.fa12, self.fa12, Nat(10)),
        )

    def change_admin(self, new_admin: Address) -> None:
        if SENDER == self.admin:
            self.admin = new_admin
        else:
            raise Exception("Not allowed")
