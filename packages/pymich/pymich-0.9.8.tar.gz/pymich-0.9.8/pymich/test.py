"""
High level API

Example:

.. code-block:: python

    loader = ContractLoader.factory('proxy/A.py')
    loader.storage['B'] = pytezos.key.public_key_hash()
    loader.storage['C'] = loader.storage['B']
    A = loader.deploy(client)
    B = loader.deploy(client)
    C = loader.deploy(client)
    D = loader.deploy(client)
    A.interface.set_B(B.address).send(min_confirmations=1)
    A.interface.set_C(C.address).send(min_confirmations=1)
    B.interface.set_B(D.address).send(min_confirmations=1)
    C.interface.set_C(A.address).send(min_confirmations=1)
    A.interface.call_B_and_C(dict(
        value_b='B',
        value_c='C',
    )).send(min_confirmations=1)

"""

import functools
from pathlib import Path
import os

from pymich.compiler import Compiler
from pytezos import ContractInterface
from pytezos.operation.result import OperationResult


class ContractLoader:
    """
    This object provides a Python API over example contracts, for testing.
    """

    def __init__(self, contract_path):
        self.contract_path = contract_path

    @functools.cached_property
    def source(self):
        with open(self.contract_path) as f:
            return f.read()

    @functools.cached_property
    def compiler(self):
        return Compiler(self.source)

    @functools.cached_property
    def micheline(self):
        return self.compiler.compile_contract()

    @functools.cached_property
    def interface(self):
        return ContractInterface.from_micheline(
            self.micheline
        )

    @property
    def dummy(self):
        return self.interface.storage.dummy()

    @classmethod
    def factory(cls, path):
        pymich = Path(os.path.dirname(__file__))
        paths = [
            Path(path),
            pymich / 'tests' / path,
            pymich / 'tests' / 'end_to_end' / path,
        ]
        for path in paths:
            if path.exists():
                return cls(path.absolute())
        raise Exception(f'{path} not found in {pymich}')

    @property
    def storage(self):
        """ Lazy mutable storage, dummy by default. """
        if '_storage' not in self.__dict__:
            self._storage = self.dummy
        return self._storage

    @storage.setter
    def storage(self, value):
        self._storage = value

    def deploy(self, pytezos):
        return ContractDeployment(self, pytezos)


class ContractDeployment:
    def __init__(self, loader, pytezos=None):
        self.loader = loader
        if pytezos:
            self.pytezos = pytezos

    @property
    def pytezos(self):
        if '_pytezos' not in self.__dict__:
            from pytezos import pytezos
            self._pytezos = pytezos
        return self._pytezos

    @pytezos.setter
    def pytezos(self, value):
        self._pytezos = value

    def using(self, **kwargs):
        self.pytezos = self.pytezos.using(**kwargs)

    @functools.cached_property
    def interface(self):
        return self.pytezos.contract(self.address)

    @functools.cached_property
    def address(self):
        return self.result[0].originated_contracts[0]

    @functools.cached_property
    def result(self):
        return OperationResult.from_operation_group(self.opg.opg_result)

    @functools.cached_property
    def opg(self):
        return self.loader.interface.using(
            shell=self.pytezos.shell,
            key=self.pytezos.key,
        ).originate(
            initial_storage=self.loader.storage,
        ).send(min_confirmations=1)

    def __getattr__(self, name):
        return getattr(self.interface, name)
