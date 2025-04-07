class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits_length = len(digits)
        for i in range(1, digits_length + 1):
            if digits[-i] == 9:
                if i == digits_length:
                    digits[-i] = 1
                    digits.append(0)
                else:
                    digits[-i] = 0
            else:
                digits[-i] = digits[-i] + 1
                break
        return digits


solution = Solution()

print(solution.plusOne([9, 9, 9]))
