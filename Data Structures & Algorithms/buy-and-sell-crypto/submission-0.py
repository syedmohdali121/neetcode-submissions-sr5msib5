class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)

        return max_profit
        