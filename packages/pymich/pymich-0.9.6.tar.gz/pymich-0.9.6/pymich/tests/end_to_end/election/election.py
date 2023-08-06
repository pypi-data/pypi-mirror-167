from dataclasses import dataclass
from pymich.michelson_types import *


def require(condition: bool, message: String) -> Nat:
    if not condition:
        raise Exception(message)

    return Nat(0)


@dataclass(kw_only=True)
class Election(BaseContract):
    admin: Address
    manifest_url: String
    manifest_hash: String
    _open: String
    _close: String
    artifacts_url: String
    artifacts_hash: String

    def open(self, _open: String, manifest_url: String, manifest_hash: String) -> None:
        require(Tezos.sender == self.admin, String("Only admin can call this entrypoint"))
        self._open = _open
        self.manifest_url = manifest_url
        self.manifest_hash = manifest_hash

    def close(self, _close: String) -> None:
        require(Tezos.sender == self.admin, String("Only admin can call this entrypoint"))
        self._close = _close

    def artifacts(self, artifacts_url: String, artifacts_hash: String) -> None:
        require(Tezos.sender == self.admin, String("Only admin can call this entrypoint"))
        self.artifacts_url = artifacts_url
        self.artifacts_hash = artifacts_hash

