# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -10**9 <= nums[i] <= 10**9

class Solution:
    def majority_element(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n // 2]

    # second solution
    #     count = 0
    #     candidate = 0
    #
    #     for num in nums:
    #         if count == 0:
    #             candidate = num
    #
    #         if num == candidate:
    #             count += 1
    #         else:
    #             count -= 1
    #
    #     return candidate


solution = Solution()


def test_solution():
    def print_result(result, expected):
        print('Ok') if result == expected else print('Fail, Result:', result)

    print("Should return 3 for [3,2,3]")
    print_result(solution.majority_element([3, 2, 3]), 3)

    print("Should return 2 for [2,2,1,1,1,2,2]")
    print_result(solution.majority_element([2, 2, 1, 1, 1, 2, 2]), 2)


test_solution()
