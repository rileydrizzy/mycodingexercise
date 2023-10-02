'''
Merge sort is a sorting algorithm that sort an unsorted array in ascending order
It use divide and conquer technique, and also recursive technique in it's approach
It has a time complexity of BIG O (nlogn) and space complextiy of BIG O (n)
'''
import random

def merge_sort(array):
    """_summary_

    Parameters
    ----------
    array : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    if len(array) == 1:
        return array
    mid_point = len(array) //2
    first_sublist = array[:mid_point]
    second_sublist = array[mid_point:]
    first_sublist = merge_sort(first_sublist)
    second_sublist = merge_sort(second_sublist)
    return _merge_(first_sublist,second_sublist)

def _merge_(first_array, second_array):
    j=i=0
    sorted_array = []
    while j < len(first_array) and i < len(second_array):
        if first_array[j] < second_array[i]:
            sorted_array.append(first_array[j])
            j+=1
        else:
            sorted_array.append(second_array[i])
            i+=1
    while j < len(first_array):
        sorted_array.append(first_array[j])
        j+=1
    while i < len(second_array):
        sorted_array.append(second_array[i])
        i+=1
    return sorted_array


def test_case():
    """ runs stress test
    """
    try:
        test = True
        for num in range(10000):
            sample_list = [random.randint(1,1000) for num in range(20)]
            sample_list_copy = sample_list.copy()
            sorted_array_ = merge_sort(sample_list)
            if sample_list_copy.sort() == sample_list:
                print(f'sample_list = {sample_list}')
                print(f'sample_list_copy = {sample_list_copy}')
                test = False
        if test is not False:
            print('Stress Testing  passed')
            print(sorted_array_ ,sample_list_copy)
        else:
            print('Stress Testing  failed')

    except Exception as error:
        print(sample_list)
        print(f'Failed as a result of {error}')

test_case()
