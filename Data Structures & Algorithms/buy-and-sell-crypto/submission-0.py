class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        max_profit = 0
        l = 0
        r = 0

        while r < len(prices):
            # increase r in an attempt to maximise profit
            max_profit = max(max_profit, prices[r] - prices[l])

            # if r < l then move l to the position of r because this is optimal
            if prices[r] < prices[l]:
                l = r
            
            r += 1
        
        return max_profit

        