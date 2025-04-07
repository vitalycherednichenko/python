# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reserve = 0
        for num in nums:
            if reserve < 0:
                return False
            if num > reserve:
                reserve = num
            reserve -= 1

        return True


solution = Solution()


def test_solution():
    def print_result(result, expected):
        print('Ok') if result == expected else print('Fail, Result:', result)

    print("Should return True for [2,3,1,1,4]")
    print_result(solution.canJump([2, 3, 1, 1, 4]), True)
    '''
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    '''

    print("Should return Failed for [3,2,1,0,4]")
    print_result(solution.canJump([3, 2, 1, 0, 4]), False)
    '''
    Explanation: You will always arrive at index 3 no matter what. 
    Its maximum jump length is 0, which makes it impossible to reach the last index.
    '''

    print("Should return True for [0, 1]")
    print_result(solution.canJump([0, 1]), False)

    print("Should return True for [0]")
    print_result(solution.canJump([0]), True)

    print("Should return True for [1]")
    print_result(solution.canJump([1]), True)

    print("Should return True for [1, 2]")
    print_result(solution.canJump([1, 2]), True)

    print("Should return True for [1, 0]")
    print_result(solution.canJump([1, 0]), True)

    print("Should return True for [2, 0]")
    print_result(solution.canJump([2, 0]), True)


test_solution()
