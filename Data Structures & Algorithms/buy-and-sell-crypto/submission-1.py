class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Edge case: if the array is empty, return 0
        if not prices:
            return 0

        # Initialize with the first day's price
        min_price = prices[0]
        max_profit = 0
        
        # We can start iterating from the second day (index 1)
        for i in range(1, len(prices)):
            price = prices[i]
            
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit