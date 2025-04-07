# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].


class Solution:
    def canJump(self, nums: list[int]) -> int:
        jumps = 0
        cur_end = 0
        cur_farthest = 0

        for i in range(len(nums) - 1):
            cur_farthest = max(cur_farthest, i + nums[i])

            if (i == cur_end):
                jumps += 1
                cur_end = cur_farthest

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

    print("Should return 2 for [2,3,0,1,0]")
    print_result(solution.canJump([2, 3, 0, 1, 0]), 2)
    #
    print("Should return 2 for [1,2,0,1]")
    print_result(solution.canJump([1,2,0,1]), 2)

    print("Should return 0 for [0]")
    print_result(solution.canJump([0]), 0)

    print("Should return 1 for [1, 0]")
    print_result(solution.canJump([1, 0]), 1)

    print("Should return 1 for [3, 2, 1]")
    print_result(solution.canJump([3, 2, 1]), 1)

    print("Should return 2 for [4, 1, 1, 3, 1, 1, 1]")
    print_result(solution.canJump([4, 1, 1, 3, 1, 1, 1]), 2)


test_solution()
