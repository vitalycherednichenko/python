class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        count = 0
        while count < min(len(word1), len(word2)):
            result += word1[count]
            result += word2[count]
            count += 1
        return result + word1[count:] + word2[count:]


solution = Solution()

print(solution.mergeAlternately("abcrtrs", "ko"))