from algorithms.sorting_algorithms.test import test


def merge_sort(array):
    if len(array) <= 1:
        return

    sep = len(array) // 2

    left = array[:sep]
    right = array[sep:]

    merge_sort(left)
    merge_sort(right)

    temp = merge(left, right)

    for i in range(len(temp)):
        array[i] = temp[i]


def merge(arr1, arr2):
    l = r = 0
    result = []

    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            result.append(arr1[l])
            l += 1
        else:
            result.append(arr2[r])
            r += 1

    while l < len(arr1):
        result.append(arr1[l])
        l += 1

    while r < len(arr2):
        result.append(arr2[r])
        r += 1

    return result


test(merge_sort)
