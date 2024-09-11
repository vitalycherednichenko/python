from algorithms.sorting_algorithms.test import test


def hoar_sort(arr):
    if len(arr) <= 1:
        return

    barrier = arr[0]

    left = []
    right = []
    middle = []

    for i in arr:
        if i < barrier:
            left.append(i)
        elif i > barrier:
            right.append(i)
        else:
            middle.append(i)

    hoar_sort(left)
    hoar_sort(right)

    temp = left + middle + right

    for i in range(len(arr)):
        arr[i] = temp[i]


test(hoar_sort)
