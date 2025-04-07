"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for char in t:
            if s and idx < len(s) and char == s[idx]:
                idx += 1
        return len(s) == idx


sol = Solution()

print(sol.isSubsequence("b", "ahbgdc"))