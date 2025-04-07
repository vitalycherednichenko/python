"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                min_height = min(height[i], height[j])
                max_area = max(max_area, min_height * (j - i))
        return max_area


sol = Solution()

print(sol.maxArea([1,8,6,2,5,4,8,3,7]))