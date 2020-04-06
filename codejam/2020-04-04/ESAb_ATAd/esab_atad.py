# 0 - complemented
# 1 - reversed
# 2 - complemented + reversed
# 3 - nothing

def guess_bits(bits: int):
    answer = [None] * bits

    layers = []

    for _ in range(15):
        layer = read_layer()
        layers.append(layer)

    print_answer(answer)

def read_layer(bits: int, offset: int) -> List[int]:
    layer = [None] * bits

    for pos in range(offset, offset + 5):
        layer[pos] = get_number_from_judge(pos)
        layer[bits - pos] = get_number_from_judge(bits - pos)

    return layer


def reverse(pos: int, array: List[int]) -> None:
    array[pos], array[len(array) - pos] = array[len(array) - pos], array[pos]

def complement(pos: int, array: List[int]) -> None:
    array[pos] = 0 if array[pos] else 1
    array[len(array) - pos] = 0 if array[len(array) - pos] else 1

def do_nothing(pos: int, array: List[int]) -> None:
    pass

def reverse_complement(pos: int, array: List[int]) -> None:
    reverse(pos, array)
    complement(pos, array)


def request_number(pos: int) -> None:
    print(pos)


def get_number_from_judge(pos: int) -> int:
    request_number(pos)
    return int(input())


def print_answer(nums: List[int]) -> None:
    print("".join(map(str, nums)))


def read_init() -> Tuple[int, int]:
    tests, bits = input().split()

    return int(tests), int(bits)


def run_tests():
    tests, bits = read_init()

    for _ in range(tests):
        guess_bits(bits)


def main():
    run_tests()


if __name__ == "__main__":
    main()
