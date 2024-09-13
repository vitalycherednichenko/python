# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
from itertools import accumulate


# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in range(0, len(prices)):
            if buy_price < prices[i]:
                profit += prices[i] - buy_price
            buy_price = prices[i]
        return profit

        # Second solution
        # for i in range(1, len(prices)):
        #     if prices[i] <= buy_price:
        #         buy_price = prices[i]
        #     else:
        #         if i == len(prices) - 1 or prices[i + 1] < prices[i]:
        #             profit += prices[i] - buy_price
        #             buy_price = prices[i]
        #
        # return profit


solution = Solution()


def test_solution():
    def print_result(result, expected):
        print('Ok') if result == expected else print('Fail, Result:', result)

    print("Should return 7 for [7,1,5,3,6,4]")
    print_result(solution.maxProfit([7, 1, 5, 3, 6, 4]), 7)
    '''
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Total profit is 4 + 3 = 7.
    '''

    print("Should return 4 for [1,2,3,4,5]")
    print_result(solution.maxProfit([1, 2, 3, 4, 5]), 4)


test_solution()
