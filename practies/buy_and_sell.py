# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price <= buy_price:
                buy_price = price

            max_profit = max(max_profit, price - buy_price)

        return max_profit


solution = Solution()


def test_solution():
    def print_result(result, expected):
        print('Ok') if result == expected else print('Fail, Result:', result)

    print("Should return 5 for [7,1,5,3,6,4]")
    print_result(solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    print("Should return 0 for [7,6,4,3,1]")
    print_result(solution.maxProfit([7,6,4,3,1]), 0)


test_solution()
