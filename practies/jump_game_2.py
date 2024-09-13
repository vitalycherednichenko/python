# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].


class Solution:
    def canJump(self, nums: list[int]) -> int:
        jumps = []

        return jumps


solution = Solution()


def test_solution():
    def print_result(result, expected):
        print('Ok') if result == expected else print('Fail, Result:', result)

    print("Should return 2 for [2,3,1,1,4]")
    print_result(solution.canJump([2, 3, 1, 1, 4]), 2)
    '''
    The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
    '''

    print("Should return 2 for [2,3,0,1,4]")
    print_result(solution.canJump([2, 3, 0, 1, 4]), 2)

    print("Should return 2 for [1,2,0,1]")
    print_result(solution.canJump([2, 3, 0, 1, 4]), 2)


test_solution()
