"""
Selection sort is an algorithm that sort an unsorted array in ascending order
It has a time complexity BIG O(n^2) of and Space Complexity of Constant space O(1)
"""
import random

def selection_sort(array):
    pass

# TEST CASE AREA
def test_case():
    '''
    runs tests cases on selection sort
    '''
    sample_list = [[random.randint(1, 30)for j in range(15)] for n in range(6)]
    for array in sample_list:
        print(selection_sort(array) == sorted(array)) #Checks and print true if array is sorted

test_case()
