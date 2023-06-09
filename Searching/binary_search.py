'''
Binary Search is a searching alogrithm that looks for a target in a sorted list,
by using divide and conquer techqniues. This Search algorithm has a time complexity of 
BIG O(logn) and Space comlextiy of Constant space O(1).
'''
import random


def binary_search(arr, key):
    """
    search for element in the given array
    
    Args: 

    """
    start_index = 0
    end_index = len(arr) - 1
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if key == arr[middle_index]:
            return middle_index
        if key > arr[middle_index]:
            start_index = middle_index + 1
        elif key < arr[middle_index]:
            end_index = middle_index - 1
    return "Not in the List"


#TEST CASE
def test_case():
    '''
    runs test case on binary search
    '''
    sample_list = [[random.randint(1,40,) for j in range(15)] for n in range(5)]
    for array in sample_list:
        array.sort()
        item = random.randint(0,14)
        print(f'List --> {array} \ntarget --> {item}')
        print(f'key index --> {binary_search(array,item)}')

test_case()
