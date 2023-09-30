"""doc
"""

import random

def binary_search(binary_array, item, first_idx, last_idx):
    while first_idx <= last_idx:
        mid_idx = (first_idx + last_idx)//2
        if binary_array[mid_idx] == item:
            return mid_idx
        if binary_array[mid_idx] < item:
            first_idx = mid_idx + 1
        else:
            last_idx = mid_idx - 1
    return False

def exponential_search(item, array):
    if array[0] == item:
        return 0
    index = 1
    while index < len(array) and item > array[index]:
        index *= 2

    return binary_search(binary_array=array, item=item, first_idx= index//2,
                         last_idx= min(index, len(array) - 1))

# Stress Test

def stress_test():
    sample = sorted([random.randint(0,500) for num in range(10)])
    item = random.choice(sample)
    answer = exponential_search(item, sample)
    return (answer, sample, item)

for no_iter in range(10000):
    result, array_, item_ = stress_test()
    if result != array_.index(item_):
        print(array_, item_)

print('Stress testing done')
