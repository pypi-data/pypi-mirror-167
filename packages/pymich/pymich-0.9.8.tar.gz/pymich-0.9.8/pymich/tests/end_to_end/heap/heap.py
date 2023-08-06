from pymich.michelson_types import *

# def my_map_add_ten(key):
#     my_map[key] += 10
def my_map_add_ten(heap: BigMap[String, Bytes], key: String) -> BigMap[String, Bytes]:
    my_map = heap[String("my_map")].unpack(Map[String, Nat])
    my_map[key] = my_map[key] + Nat(10)
    heap[String("my_map")] = Bytes(my_map)
    return heap

class Pointers(BaseContract):
    a: Nat
    b: Nat

    def add(self) -> None:
        heap = BigMap[String, Bytes]()

        # my_map = {"a": 0}
        my_map_key_to_update = String("a")
        my_map = Map[String, Nat]().add(my_map_key_to_update, Nat(0))
        heap[String("my_map")] = Bytes(my_map)


        # my_map_add_ten(my_map_key_to_update)
        heap = my_map_add_ten(heap, my_map_key_to_update)

        # self.a = my_map[my_map_key_to_update]
        self.a = heap[String("my_map")].unpack(Map[String, Nat])[my_map_key_to_update]

    def sub(self) -> None:
        self.b = Nat(1)
