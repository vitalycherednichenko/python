"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""


class Solution:
    def compress(self, chars: list[str]) -> int:
        current_char = ''
        count = 0
        i = 0
        while i < len(chars):
            if chars[i] != current_char:
                current_char = chars[i]
                count = 0
            count += 1

            if count > 1 and ((i == len(chars) - 1) or (chars[i + 1] != current_char))  :
                i = i - (count - 2)

                for digit in str(count):
                    chars[i] = digit
                    i += 1

                while i < len(chars) and chars[i] == current_char:
                    chars.pop(i)
                continue

            i += 1
        return len(chars)


sol = Solution()
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b", 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'f', "b","b","b",]))
