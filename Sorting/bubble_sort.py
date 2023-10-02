"""
Bubble Sort is an algorithm that sort an unsorted array in ascending order
It has a time complexity BIG O(n^2) of and Space Complexity of Constant space O(1)
"""

import random
import copy
def bubble_sort(array):
    """_summary_

    Parameters
    ----------
    array : _type_
        _description_
    """
    no_iter = len(array) - 1
    for outer in range(no_iter, 0, -1):
        for inner in range(outer):
            if array[inner] > array[inner + 1]:
                array[inner], array[inner + 1] = array[inner+1], array[inner]


#Stress Test
def test_case():
    """ runs stress test
    """
    try:
        test = True
        for num in range(10000):
            sample_list = [random.randint(1,1000) for num in range(20)]
            sample_list_copy = sample_list.copy()
            bubble_sort(sample_list)
            if sample_list_copy.sort() == sample_list:
                print(f'sample_list = {sample_list}')
                print(f'sample_list_copy = {sample_list_copy}')
                test = False
        if test is not False:
            print('Stress Testing  passed')
        else:
            print('Stress Testing  failed')

    except Exception as error:
        print(sample_list)
        print(f'Failed as a result of {error}')

test_case()
