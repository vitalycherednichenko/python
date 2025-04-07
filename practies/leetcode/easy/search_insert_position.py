class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0

        for i, num in enumerate(nums):
            if num == target or num > target:
                return i
            if i == len(nums) - 1 and num > target:
                return i + 1

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


solution = Solution()

print(solution.searchInsert([1, 4, 5, 7], 3))
