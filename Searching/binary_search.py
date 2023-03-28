'''
Searching 
'''
import random
# Binary Search


def binary_search(arr, key):
    '''
    explain
    '''
    start_index = 0
    end_index = len(arr) - 1
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if key == arr[middle_index]:
            return middle_index
        elif key > arr[middle_index]:
            start_index = middle_index + 1
        elif key < arr[middle_index]:
            end_index = middle_index - 1
    return "Not in the List"


# TEST CASE
sample = [[random.randint(1,30,) for j in range(15)] for n in range(5)]
for n in sample:
    n.sort()
    random_index = random.randint(0,14)
    item = n[random_index]
    print('List and key')
    print(n, item )
    print('key index')
    print(binary_search(n, item))
