# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(number: int) -> int:
    first_divider: int = 3
    second_divider: int = 5
    sum_result: int = 0

    if number > first_divider:
        for i in range(first_divider, number):
            sum_result += i if i % first_divider == 0 or i % second_divider == 0 else 0

    return sum_result


def test_solution():
    def print_result(result, expected):
        print('Ok') if result == expected else print('Fail, Result:', result)

    print("Should return 0 for n=3")
    print_result(solution(3), 0)

    print("Should return 0 for n=0")
    print_result(solution(0), 0)

    print("Should return 0 for n=-1")
    print_result(solution(-1), 0)

    print("Should return 3 for n=4")
    print_result(solution(4), 3)

    print("Should return 8 for n=6")
    print_result(solution(6), 8)

    print("Should return 60 for n=16")
    print_result(solution(16), 60)

    print("Should return 3 for n=5")
    print_result(solution(5), 3)

    print("Should return 45 for n=15")
    print_result(solution(15), 45)

    print("Should return 23 for n=10")
    print_result(solution(10), 23)

    print("Should return 78 for n=20")
    print_result(solution(20), 78)

    print("Should return 9168 for n=200")
    print_result(solution(200), 9168)


test_solution()
