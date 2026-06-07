class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_b = prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell - min_b)
            min_b = min(min_b, sell)
        return max_profit