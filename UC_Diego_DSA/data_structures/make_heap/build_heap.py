# python3


def build_heap(data, size):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []

    def minichild(idx):
        if idx * 2 + 2 > size:
            return idx * 2 + 1
        if data[idx * 2 + 1] < data[idx * 2 + 2]:
            return idx * 2 + 1
        return idx * 2 + 2

    def shiftdown(idx):
        while idx * 2 + 1 < size:
            mc = minichild(idx)
            if data[mc] < data[idx]:
                data[mc], data[idx] = data[idx], data[mc]
                swaps.append((idx, mc))
            idx = mc

    no_iter = size // 2
    for idx in range(no_iter, -1, -1):
        shiftdown(idx)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data, size=n)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
