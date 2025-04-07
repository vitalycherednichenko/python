"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero_length = 0
        i = 0

        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zero_length += 1
                continue
            i += 1

        for i in range(zero_length):
            nums.append(0)

        print(nums)



sol = Solution()

print(sol.moveZeroes([0,1,0,3,12]))