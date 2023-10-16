"""doc
"""
import random


def interpolation_search(array, item):
    """_summary_

    Parameters
    ----------
    array : _type_
        _description_
    item : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    first_idx, last_idx = 0, len(array) - 1
    while first_idx <= last_idx:
        mid_idx = first_idx + (
            (last_idx - first_idx)
            * (item - array[first_idx])
            / (array[last_idx] - array[first_idx])
        )
        mid_idx = int(mid_idx)
        if array[mid_idx] == item:
            return mid_idx
        if item > array[mid_idx]:
            first_idx = mid_idx + 1
        else:
            last_idx = mid_idx - 1
    return -1


# STRESS TEST
def stress_test():
    """_summary_"""

    def random_sorted_list():
        sample_arr = sorted(random.sample(range(0, 1000 + 1), 10))
        item = random.choice(sample_arr)
        answer = interpolation_search(sample_arr, item)
        return (answer, sample_arr, item)

    for _ in range(1000000):
        result, array_, item_ = random_sorted_list()
        if result != array_.index(item_):
            print(array_, item_)
    print("Stress testing done")


stress_test()
