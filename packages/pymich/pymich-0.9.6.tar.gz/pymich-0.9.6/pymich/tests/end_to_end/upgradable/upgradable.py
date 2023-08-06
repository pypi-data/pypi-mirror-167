from dataclasses import dataclass

from pymich.michelson_types import *
from typing import Callable


@dataclass(kw_only=True)
class Upgradable(BaseContract):
    counter: Nat
    f: Callable[[Nat], Nat]

    def update_f(self, f: Callable[[Nat], Nat]) -> None:
        self.f = f

    def update_counter(self, x: Nat) -> None:
        self.counter = self.f(x)
