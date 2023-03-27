'''
sorting
'''
# Bubble Sort


def bubble_sort(arr):
    '''' 
    bubblesort
    '''
    len_arr = len(arr) - 1
    for j in range(len_arr, 0, -1):
        for i in range(j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return
#TEST CASES AREA 
sample = [2,46,7,32,8,32,4,2,15,67,9]
bubble_sort(sample)
print(sample)