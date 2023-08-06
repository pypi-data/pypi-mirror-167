import unittest
from pymich.michelson_types import String, Address, Tezos
from pymich.tests.end_to_end.election.election import Election

Tezos.sender.address = "Mrs. Foo"

def get_contract(sender):
    return Election(
        admin=sender,
        manifest_url=String(""),
        manifest_hash=String(""),
        _open=String(""),
        _close=String(""),
        artifacts_url=String(""),
        artifacts_hash=String("")
    )


class TestContract(unittest.TestCase):
    def test_open(self):
        contract = get_contract(Tezos.sender)
        _open, _url, _hash = String("foo"), String("bar"), String("baz")
        contract.open(_open, _url, _hash)

        assert contract._open == _open
        assert contract.manifest_url == _url
        assert contract.manifest_hash == _hash

        contract = get_contract(Address("yolo"))
        try:
            contract.open(_open, _url, _hash)
            assert 0
        except Exception as e:
            assert e.args[0].value == 'Only admin can call this entrypoint'

    def test_close(self):
        contract = get_contract(Tezos.sender)
        close = String("foo")
        contract.close(close)

        assert contract._close == close

        contract = get_contract(Address("yolo"))
        try:
            contract.close(String("foo"))
            assert 0
        except Exception as e:
            assert e.args[0].value == 'Only admin can call this entrypoint'

    def test_artifacts(self):
        contract = get_contract(Tezos.sender)
        url, hash = String("url"), String("hash")
        contract.artifacts(url, hash)

        assert contract.artifacts_url == url
        assert contract.artifacts_hash == hash

        contract = get_contract(Address("yolo"))
        try:
            contract.artifacts(url, hash)
            assert 0
        except Exception as e:
            assert e.args[0].value == 'Only admin can call this entrypoint'

if __name__ == "__main__":
    unittest.main()
