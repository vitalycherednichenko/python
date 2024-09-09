def test(func):
    arr = list(range(10)) + list(range(20, 9, -1))
    func(arr)
    print('Test case 1: result -', arr == list(range(0, 21, 1)))

    arr = [-1, 0, 9, 10, 33, 5, 9, 1]
    func(arr)
    print('Test case 2: result -', arr == [-1, 0, 1, 5, 9, 9, 10, 33])

    arr = [2, 1]
    func(arr)
    print('Test case 3: result -', arr == [1, 2])