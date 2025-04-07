class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1].lstrip()
        space_idx = s.find(' ')
        return space_idx if space_idx != -1 else len(s)



solution = Solution()

print(solution.lengthOfLastWord("hello world"))