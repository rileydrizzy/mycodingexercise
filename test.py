egde_case_arr = [[150, 181, 209, 253, 347, 397, 407, 428, 454, 469],
[85, 115, 258, 319, 366, 370, 374, 473, 484, 494],
[40, 176, 212, 250, 273, 295, 295, 338, 366, 382]]
egde_case_item =[347,473, 295]


def interpolation_search(item,array):
    first_idx = 0
    last_idx = len(array) -1
    try:
        while first_idx <= last_idx:
            mid_idx = first_idx + ((last_idx - first_idx)/(array[last_idx] - array[first_idx]))* (item - array[first_idx])
            mid_idx = int(mid_idx)
            if array[mid_idx] == item:
                return mid_idx
            if item > array[mid_idx]:
                first_idx = mid_idx + 1
            else:
                last_idx = mid_idx - 1
        return False
    except ZeroDivisionError:
        print(f'{array}, {item}, failed because of ZeroDivision')

for idx, array_ in enumerate(egde_case_arr):
    answer = interpolation_search(egde_case_item[idx], array_)
    print(answer)
    