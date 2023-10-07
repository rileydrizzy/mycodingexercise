"""
Selection sort is an algorithm that sort an unsorted array in ascending order
It has a time complexity BIG O(n^2) of and Space Complexity of Constant space O(1)
"""

import random

def selection_sort(array):
    no_element = len(array)
    for num in range(no_element):
        min_val = num
        for j in range(num+1, no_element):
            if array[j] < array[min_val]:
                min_val = j
        array[num], array[min_val] = array[min_val], array[num]

# TEST CASE AREA
for _ in range(5):
    sample_list = [random.randint(1,1000) for num in range(20)]
    sample_list_copy = sorted(sample_list)
    sample_list_copy.append(2)
    selection_sort(sample_list)
    print(f'sample_list = {sample_list}')
    print(f'sample_list_copy = {sample_list_copy}')
    