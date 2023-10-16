"""doc
"""

import random


def binary_search(binary_array, item, first_idx, last_idx):
    """_summary_

    Parameters
    ----------
    binary_array : _type_
        _description_
    item : _type_
        _description_
    first_idx : _type_
        _description_
    last_idx : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    while first_idx <= last_idx:
        mid_idx = (first_idx + last_idx) // 2
        if binary_array[mid_idx] == item:
            return mid_idx
        if binary_array[mid_idx] < item:
            first_idx = mid_idx + 1
        else:
            last_idx = mid_idx - 1
    return False


def exponential_search(item, array):
    """_summary_

    Parameters
    ----------
    item : _type_
        _description_
    array : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    if array[0] == item:
        return 0
    index = 1
    while index < len(array) and item > array[index]:
        index *= 2

    return binary_search(
        binary_array=array,
        item=item,
        first_idx=index // 2,
        last_idx=min(index, len(array) - 1),
    )


# Stress Test


# STRESS TEST
def stress_test():
    """_summary_"""

    def random_sorted_list():
        sample = sorted(random.sample(range(0, 1000 + 1), 10))
        item = random.choice(sample)
        answer = exponential_search(item, sample)
        return (answer, sample, item)

    for _ in range(10000):
        result, array_, item_ = random_sorted_list()
        if result != array_.index(item_):
            print(array_, item_)
    print("Stress testing done")


stress_test()
