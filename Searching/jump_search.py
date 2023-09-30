"""doc
"""

import random
import math

def linear_search(item, array):
    no_iterations = len(array)
    for index in range(no_iterations):
        if array[index] == item:
            return index
        elif item < array[index]:
            return - 1
    return -1

def jump_search(item ,ordered_array):
    block_size = int(math.sqrt(len(ordered_array)))
    current_idx = 0
    list_size = len(ordered_array)
    while current_idx != list_size and item >= ordered_array[current_idx]:
        if current_idx + block_size > len(ordered_array):
            block_size = len(ordered_array) - 1
            block_array = ordered_array[current_idx:current_idx+ block_size]
            j = linear_search(item, block_array)
            if j == -1:
                return False
            return current_idx + j

        if ordered_array[current_idx + block_size -1] == item:
            return current_idx + block_size -1

        if ordered_array[current_idx + block_size -1] > item:
            block_array = ordered_array[current_idx: current_idx + block_size -1]
            j = linear_search(item, block_array)
            if j == -1:
                return False
            return current_idx + j
        current_idx= current_idx + block_size

#STRESS TEST
def stress_test():
    sample = sorted([random.randint(0,500) for num in range(10)])
    item = random.choice(sample)
    answer = jump_search(item, sample)
    return (answer, sample, item)

for no_iter in range(1000):
    result, array_, item_ = stress_test()
    if result != array_.index(item_):
        print(array_, item_)

print('Stress testing done')
