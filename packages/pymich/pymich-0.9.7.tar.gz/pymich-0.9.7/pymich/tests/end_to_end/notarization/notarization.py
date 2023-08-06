from dataclasses import dataclass
from pymich.michelson_types import *


@dataclass(eq=False)
class DocumentId(Record):
    owner: Address
    uuid: String


@dataclass(kw_only=True)
class Notarization(BaseContract):
    admin: Address
    document_hashes: BigMap[DocumentId, Bytes]

    def add_document(self, document_uuid: String, document_hash: Bytes) -> None:
        self.document_hashes[DocumentId(Tezos.sender, document_uuid)] = document_hash

    def get_hash(self, document_uuid: String, owner: Address) -> Bytes:
        return self.document_hashes[DocumentId(owner, document_uuid)]
