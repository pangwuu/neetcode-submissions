class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        diff = [0] * len(prices)
        for index, price in enumerate(prices):
            if index < len(prices) - 1 and price < prices[index + 1]:
                diff[index] = prices[index + 1] - price
        
        return sum(diff)
