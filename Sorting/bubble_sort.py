'''
Bubble Sort is an algorithm that sort an unsorted array in ascending order
It has a time complexity BIG O(n^2) of and Space Complexity of Constant space O(1)
'''
import random # use to create test cases


def bubble_sort(arr):
    ''''
    The function takes in an array and return the 
    array sorted in ascending order
    '''
    len_arr = len(arr) - 1
    for j in range(len_arr, 0, -1):
        for i in range(j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# TEST CASES AREA
sample_list = [[random.randint(1,40,) for j in range(15)] for n in range(5)]
for array in sample_list:
    print(bubble_sort(array) == sorted(array)) #Checks and print true if array is sorted
