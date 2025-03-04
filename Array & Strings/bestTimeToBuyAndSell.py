# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("INF")
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            diff = i - min_price
            if diff > max_profit:
                max_profit = diff
        
        return max_profit
