"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        temp_vowels = ''

        for char in s:
            if char.lower() in vowels:
                temp_vowels = char + temp_vowels

        count = 0

        for i in range(len(s)):
            if s[i].lower() in vowels:
                s = s[:i] + temp_vowels[count] + s[i + 1:]
                count += 1

        return s


sol = Solution()

print(sol.reverseVowels('IceCreAm'))
