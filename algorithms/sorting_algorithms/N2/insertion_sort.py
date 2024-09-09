from algorithms.sorting_algorithms.test import test

def insertion_sort(array):
    for i in range(1, len(array)):
        k: int = i
        while k > 0 and array[k] < array[k - 1]:
            array[k], array[k - 1] = array[k - 1], array[k]
            k -= 1


test(insertion_sort)