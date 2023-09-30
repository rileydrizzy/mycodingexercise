"""doc
"""
import random


def interpolation_search(item,array):
    first_idx = 0
    last_idx = len(array) -1
    try:
        while first_idx <= last_idx:
            mid_idx = first_idx + ((last_idx - first_idx)/(array[last_idx] - array[first_idx]))* (item - array[first_idx])
            mid_idx = int(mid_idx)
            if array[mid_idx] == item:
                return mid_idx
            if item > array[mid_idx]:
                first_idx = mid_idx + 1
            else:
                last_idx = mid_idx - 1
        return False
    except ZeroDivisionError:
        print(f'{array}, {item}, failed because of ZeroDivision')

#STRESS TEST
def stress_test():
    sample = sorted([random.randint(0,500) for num in range(10)])
    item = random.choice(sample)
    answer = interpolation_search(item, sample)
    return (answer, sample, item)

for no_iter in range(100):
    result, array_, item_ = stress_test()
    if result != array_.index(item_):
        print(array_, item_)

print('Stress testing done')