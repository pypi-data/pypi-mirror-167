from dataclasses import dataclass
from pymich.michelson_types import *


@dataclass#(eq=True, frozen=True)
class OperatorKey(Record):
    owner: Address
    operator: Address
    token_id: Nat

@dataclass#(eq=True, frozen=True)
class LedgerKey(Record):
    owner: Address
    token_id: Nat

@dataclass#(eq=True, frozen=True)
class TokenMetadata(Record):
    token_id: Nat
    token_info: Map[String, Bytes]

@dataclass
class TransactionInfo(Record):
    to_: Address
    token_id: Nat
    amount: Nat

@dataclass
class TransferArgs(Record):
    from_: Address
    txs: List[TransactionInfo]


def require_owner(owner: Address) -> Nat:
    if Tezos.sender != owner:
        raise Exception("FA2_NOT_CONTRACT_ADMINISTRATOR")

    return Nat(0)


@dataclass(kw_only=True)
class FA2(BaseContract):
    ledger: BigMap[LedgerKey, Nat]
    operators: BigMap[OperatorKey, Nat]
    token_total_supply: BigMap[Nat, Nat]
    token_metadata: BigMap[Nat, TokenMetadata]
    owner: Address

    def create_token(self, metadata: TokenMetadata) -> None:
        require_owner(self.owner)

        new_token_id = metadata.token_id

        if new_token_id in self.token_metadata:
            raise Exception("FA2_DUP_TOKEN_ID")
        else:
            self.token_metadata[new_token_id] = metadata
            self.token_total_supply[new_token_id] = Nat(0)

    def mint_tokens(self, owner: Address, token_id: Nat, amount: Nat) -> None:
        require_owner(self.owner)

        if not token_id in self.token_metadata:
            raise Exception("FA2_TOKEN_DOES_NOT_EXIST")

        ledger_key = LedgerKey(owner, token_id)
        self.ledger[ledger_key] = self.ledger.get(ledger_key, Nat(0)) + amount
        self.token_total_supply[token_id] = self.token_total_supply[token_id] + amount

    def transfer(self, transactions: List[TransferArgs]) -> None:
        for transaction in transactions:
            for tx in transaction.txs:
                if not tx.token_id in self.token_metadata:
                    raise Exception("FA2_TOKEN_UNDEFINED")
                else:
                    if not (transaction.from_ == Tezos.sender or OperatorKey(transaction.from_, Tezos.sender, tx.token_id) in self.operators):
                        raise Exception("FA2_NOT_OPERATOR")

                    from_key = LedgerKey(transaction.from_, tx.token_id)
                    from_balance = self.ledger.get(from_key, Nat(0))

                    if tx.amount > from_balance:
                        raise Exception("FA2_INSUFFICIENT_BALANCE")

                    self.ledger[from_key] = abs(from_balance - tx.amount)

                    to_key = LedgerKey(tx.to_, tx.token_id)
                    self.ledger[to_key] = self.ledger.get(to_key, Nat(0)) + tx.amount

    def updateOperator(self, owner: Address, operator: Address, token_id: Nat, add_operator: bool) -> None:
        if Tezos.sender != owner:
            raise Exception("FA2_NOT_OWNER")

        operator_key = OperatorKey(owner, operator, token_id)
        if add_operator:
            self.operators[operator_key] = Nat(0)
        #else:
        #    del self.operators[operator_key]

    def balanceOf(self, owner: Address, token_id: Nat) -> Nat:
        if not token_id in self.token_metadata:
            raise Exception("FA2_TOKEN_UNDEFINED")

        return self.ledger.get(LedgerKey(owner, token_id), Nat(0))
