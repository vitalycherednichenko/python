from algorithms.sorting_algorithms.test import test

def selection_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]


test(selection_sort)
