"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        cache = {}
        for i in range(len(nums)):
            temp = 1
            if nums[i] in cache:
                temp = cache[nums[i]]
            else:
                for n in range(len(nums)):
                    if i == n:
                        continue
                    temp *= nums[n]

            cache[nums[i]] = temp
            result.append(temp)
        return result


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4]))
