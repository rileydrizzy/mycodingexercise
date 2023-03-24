'''
Binary  Search Algorithm is a sorting algo
'''


def binary_search(arr, key):
    ''' 
    takes the list_array to be sorted
    '''
    start_arr = 0
    end_arr = len(arr) - 1
    while start_arr <= end_arr:
        mid_arr = start_arr + end_arr // 2
        if arr[mid_arr] == key:
            return mid_arr
        elif arr[mid_arr] > key:
            start_arr = mid_arr + 1
        elif arr[mid_arr] < key:
            end_arr = mid_arr - 1
        if start_arr > end_arr:
            return None

def test_case():
    ''' 
    test cases
    '''
    test_arr = [1,4,11,25,32,37,40,43,47,49,53,55]
    test_key = 4
    ans = binary_search(test_arr,test_key)
    print(ans)

test_case()
