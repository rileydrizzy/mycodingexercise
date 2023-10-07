"""doc
"""
import random

def insertion_sort(array)-> None:
    """_summary_

    Parameters
    ----------
    array : _type_
        _description_
    """
    for index in range(1, len(array)):
        sorted_idx = index
        unsoretd_element = array[index]
        while sorted_idx > 0 and array[sorted_idx-1] > unsoretd_element:
            array[sorted_idx] = array[sorted_idx-1]
            sorted_idx-=1
        array[sorted_idx] = unsoretd_element

#Stress Test
def test_case():
    """ runs stress test
    """
    try:
        for num in range(5):
            sample_list = [random.randint(1,1000) for num in range(20)]
            sample_list_copy = sorted(sample_list)
            sample_list_copy.append(2)
            insertion_sort(sample_list)
            if sample_list_copy == sample_list:
                print(f'sample_list = {sample_list}')
                print(f'sample_list_copy = {sample_list_copy}')

    except Exception as error:
        print(sample_list)
        print(f'Failed as a result of {error}')

test_case()
