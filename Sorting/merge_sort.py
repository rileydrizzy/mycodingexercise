'''
Merge sort is a sorting algorithm that sort an unsorted array in ascending order
It use divide and conquer technique, and also recursive technique in it's approach
It has a time complexity of BIG O (nlogn) and space complextiy of BIG O (n)
'''
import random # use to create test cases

def merge_sortr(arr):
    '''
    It takes in an array and divides it
    And then pass it to the merge function and return a sorted list
    '''
    len_arr = len(arr)
    if len_arr == 1:
        return arr
    mid_point = len_arr//2
    first_half = arr[:mid_point]
    second_half = arr[mid_point:]
    #Each half of the array is pass back to the function, recursively
    first_sub = merge_sortr(first_half)
    second_sub = merge_sortr(second_half)
    return merge(first_sub, second_sub)


def merge(first_sub, second_sub):
    '''
   It take in two array and sort them by repeatedly taking the low value
   and appending it to the sorted_list array 
   After which it return the sorted_list array
    '''
    i = j = 0
    sorted_list = []
    while i < len(first_sub) and j < len(second_sub):
        if first_sub[i] < second_sub[j]:
            sorted_list.append(first_sub[i])
            i += 1
        else:
            sorted_list.append(second_sub[j])
            j += 1
    while i < len(first_sub):
        sorted_list.append(first_sub[i])
        i += 1
    while j < len(second_sub):
        sorted_list.append(second_sub[j])
        j += 1
    return sorted_list


# TEST CASE AREA

def test_case():
    '''
    runs test cases for the merge sort algorithm
    '''
    sample_list= [[random.randint(1, 30) for k in range(10)] for n in range(5)]
    for num in sample_list:
        print(f'Unsoretd -> {num}')
        print(f'Sorted -> {merge_sortr(num)== sorted(num)}')

test_case()
