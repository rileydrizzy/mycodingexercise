'''
Explain selection sort
'''
import random


def selection_sort(arr):
    '''
    explain
    '''
    iteration_no = len(arr)
    for j in range(iteration_no):
        low_value_index = j
        for k in range(j+1, iteration_no):
            if arr[low_value_index] > arr[k]:
                low_value_index = k
        arr[j], arr[low_value_index] = arr[low_value_index], arr[j]

# TEST CASE AREA
sample = [[random.randint(1, 30)for j in range(15)] for n in range(3)]
for n in sample:
    print('Unsorted array', n)
    selection_sort(n)
    print('Sorted array using selection sort', n)
