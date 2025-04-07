"""
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2) and str1 != str2:
            return ''

        while len(str1) != len(str2):

            min_len = min(len(str1), len(str2))

            if str1[:min_len] != str2[:min_len]:
                return ''

            temp_str = str1[min_len:] + str2[min_len:]

            str1 = str1[:min_len]
            str2 = temp_str

        return str1 if str1 == str2 else ''


solution = Solution()

print(solution.gcdOfStrings("LEET", "CODE"))
