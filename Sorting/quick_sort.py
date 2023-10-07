"""doc
"""
import random


def quick_sort(array,first_idx, last_idx):
    if last_idx - first_idx <= 0:
        return
    else:
        partion_idx = partion_func(array,first_idx,last_idx)
        quick_sort(array, first_idx, partion_idx -1)
        quick_sort(array, partion_idx +1, last_idx)

def partion_func(array, first_idx, last_idx):
    piviot_idx = first_idx
    piviot_val = array[first_idx]
    greater_than_idx = first_idx + 1
    #idx_of_last_element = last_idx
    lesser_than_idx = last_idx

    while True:
        while piviot_val > array[greater_than_idx] and greater_than_idx < last_idx:
            greater_than_idx+=1

        while piviot_val < array[lesser_than_idx] and lesser_than_idx >= first_idx:
            lesser_than_idx-=1
        if  greater_than_idx < lesser_than_idx:
            array[greater_than_idx], array[lesser_than_idx] = array[lesser_than_idx],\
                array[greater_than_idx]
        else:
            break
    array[piviot_idx] = array[lesser_than_idx]
    array[lesser_than_idx] = piviot_val
    return lesser_than_idx

# TEST CASE AREA
for _ in range(3):
    sample_arr = [random.randint(1,10) for num in range(20)]
    sample_list_copy = sorted(sample_arr)
    quick_sort(sample_arr, 0 , len(sample_arr) - 1)
    print(f'sample_list = {sample_arr}')
    print(f'sample_list_copy = {sample_list_copy}')
