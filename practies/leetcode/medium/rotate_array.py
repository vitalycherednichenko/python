# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Constraints:
# 1 <= nums.length <= 105
# -2**31 <= nums[i] <= 2**31 - 1
# 0 <= k <= 105

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if len(nums) <= k:
            k %= len(nums)
        extend_array = nums[:-k]
        del nums[:-k]
        nums.extend(extend_array)

        # for i in range(k):
        #     nums.insert(0, nums.pop())



solution = Solution()


def test_solution():
    def print_result(result, expected):
        print('Ok') if result == expected else print('Fail, Result:', result)

    print("Should return [5,6,7,1,2,3,4] for nums = [1,2,3,4,5,6,7], k = 3")
    arr = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(arr, 3)
    print_result(arr, [5, 6, 7, 1, 2, 3, 4])

    print("Should return [3,99,-1,-100] for nums = [-1,-100,3,99], k = 2")
    arr = [-1, -100, 3, 99]
    solution.rotate(arr, 2)
    print_result(arr, [3, 99, -1, -100])

    print("Should return [1,2] for nums = [1,2], k = 3")
    arr = [1, 2]
    solution.rotate(arr, 3)
    print_result(arr, [2, 1])


test_solution()
