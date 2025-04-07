class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(int(a, 2) + int(b, 2))

        return bin(int(a, 2) + int(b, 2))[2:]


sol = Solution()
print(sol.addBinary("1010", "1011"))