"""
Binary Search is a searching alogrithm that looks for a target in a sorted list,
by using divide and conquer techqniues. This Search algorithm has a time complexity of 
BIG O(logn) and Space comlextiy of Constant space O(1).
"""
import random
import numpy as np

def binary_search(item,array):
    first_index = 0
    last_index = len(array)-1
    while first_index <= last_index:
        mid_point = (first_index + last_index)//2
        if array[mid_point] == item:
            return mid_point
        if item > array[mid_point]:
            first_index = mid_point + 1
        else:
            last_index = mid_point - 1
    return False

#STRESS TEST
def stress_test():
    sample = sorted(np.random.randint(1,500,size=10))
    item = random.choice(sample)
    answer = binary_search(item, sample)
    return (answer, sample, item)

for no_iter in range(100):
    result, array_, item_ = stress_test()
    if result != array_.index(item_):
        print(array_, item_)

print('Stress testing done')
