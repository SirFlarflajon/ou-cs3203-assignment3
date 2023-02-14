def sum_arr(arr):
    arr_sum = 0
    for x in arr:
        arr_sum += x
    return arr_sum


if __name__ == '__main__':
    arr1 = [12, 45, 5]
    arr2 = [2.0, 3.45, 6.375]
    print(sum_arr(arr1))
    print(sum_arr(arr2))
