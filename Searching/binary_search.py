"""
Binary Search is a searching alogrithm that looks for a target in a sorted list,
by using divide and conquer techqniues. This Search algorithm has a time complexity of 
BIG O(logn) and Space comlextiy of Constant space O(1).
"""
import random


def binary_search(item, array):
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
    first_index = 0
    last_index = len(array) - 1
    while first_index <= last_index:
        mid_point = (first_index + last_index) // 2
        if array[mid_point] == item:
            return mid_point
        if item > array[mid_point]:
            first_index = mid_point + 1
        else:
            last_index = mid_point - 1
    return False


# STRESS TEST
def stress_test():
    """_summary_"""

    def random_sorted_list():
        sample = sorted(random.sample(range(0, 1000 + 1), 10))
        item = random.choice(sample)
        answer = binary_search(item, sample)
        return (answer, sample, item)

    for _ in range(10000):
        result, array_, item_ = random_sorted_list()
        if result != array_.index(item_):
            print(array_, item_)
    print("Stress testing done")


stress_test()
