from typing import Union
import pymich.michelson_types as t


def transaction(
    contract: t.Contract[t.ParameterType], amount: t.Mutez, type: t.ParameterType
) -> t.Operation:
    return t.Operation()


def len(
    data: Union[
        t.BigMap[t.KeyType, t.ValueType],
        t.Map[t.KeyType, t.ValueType],
        t.Set[t.ValueType],
        t.List[t.ValueType],
        t.String,
        t.Bytes,
    ]
) -> t.Nat:
    return data.__nat_len__()
