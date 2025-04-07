class Solution:
    def mergeTwoLists(self, list1, list2):
        list1.extend(list2)
        list1.sort()
        return list1


solution = Solution()

print(solution.mergeTwoLists([1, 2, 3, 4, 5], [6, 7, 8, 9]))
