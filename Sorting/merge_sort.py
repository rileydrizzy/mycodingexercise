'''
Merge sort is a sorting algorithm that sort an unsorted array in ascending order
It use divide and conquer technique, and also recursive technique in it approach
It has a time complexity of and space complextiy of 
'''
import random # use to create test cases


def merge_sort(arr):
    '''
    This func takes in an array
    '''
    len_arr = len(arr)
    if len_arr == 1:
        return arr
    mid_point = len_arr//2
    first_half = arr[:mid_point]
    second_half = arr[mid_point:]
    #
    first_sub = merge_sort(first_half)
    second_sub = merge_sort(second_half)
    return merge(first_sub, second_sub)


def merge(first_sub, second_sub):
    '''
    explain func
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


sample_list= [[random.randint(1, 30) for k in range(10)] for n in range(5)]
for num in sample_list:
    print(f'Unsoretd -> {num}')
    print(f'Sorted -> {merge_sort(num)== sorted(num)}')
