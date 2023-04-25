'''
Selection sort is an algorithm that sort an unsorted array in ascending order
It has a time complexity BIG O(n^2) of and Space Complexity of Constant space O(1)
'''
import random # use to create test cases


def selection_sort(arr):
    '''
    The function takes in an array and return the 
    array sorted in ascending order
    '''
    iteration_no = len(arr)
    for j in range(iteration_no):
        low_value_index = j
        for k in range(j+1, iteration_no):
            if arr[low_value_index] > arr[k]:
                low_value_index = k
        arr[j], arr[low_value_index] = arr[low_value_index], arr[j]
    return arr

# TEST CASE AREA
sample_list = [[random.randint(1, 30)for j in range(15)] for n in range(6)]
for array in sample_list:
    print(selection_sort(array) == sorted(array)) #Checks and print true if array is sorted
