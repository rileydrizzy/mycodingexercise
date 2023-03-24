'''
Binary  Search Algorithm is a sorting algo
'''


def binary_search(arr, key):
    ''' 
    takes the array to be sorted
    '''
    start_arr = 0
    end_arr = len(arr) - 1
    while start_arr < end_arr:
        mid_arr = start_arr + end_arr // 2
        if arr[mid_arr] == key:
            return arr[mid_arr]
        break
        elif arr[mid_arr] > key:
            start_arr = arr[mid_arr] + 1
        elif arr[mid_arr] < key:
            end_arr = arr[mid_arr] - 1
    if start_arr > end_arr:
        return None


def test_case():
    ''' 
    test cases
    '''
    arr = [10,30,100,120,500]
    key = 10
    ans = binary_search(arr, key)
    return ans

final = test_case()
print(final)
