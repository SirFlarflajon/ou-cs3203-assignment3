def sum_arr(arr):
    arr_sum = 0
    for x in arr:
        arr_sum += x
    return arr_sum


def prod_arr(arr):
    arr_prod = 1
    for x in arr:
        if x == 0:
            continue
        arr_prod = x * arr_prod
    return arr_prod


def swap_arr(arr):
    rev_arr = []
    for x in arr:
        rev_arr = [x] + rev_arr
    return rev_arr


if __name__ == '__main__':
    # Array tests, using both integers and double
    arr1 = [12, 45, 5]
    arr2 = [2.0, 3.45, 6.375]
    arr3 = [0, 2, 3, 2]
    arr4 = [0.25, 0.0, 1.25]
    # Testing out sum_arr
    print(sum_arr(arr1))
    print(sum_arr(arr2))
    print(sum_arr(arr3))
    print(sum_arr(arr4))
    # Testing out prod_arr
    print(prod_arr(arr1))
    print(prod_arr(arr2))
    print(prod_arr(arr3))
    print(prod_arr(arr4))
    # Testing out swap_arr
    print(swap_arr(arr1))
    print(swap_arr(arr2))
    print(swap_arr(arr3))
    print(swap_arr(arr4))
