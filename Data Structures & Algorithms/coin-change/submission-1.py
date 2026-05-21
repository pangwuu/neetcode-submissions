class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1] * (amount + 1)
        
        dp[0] = 0

        for coin in coins:
            if coin > amount:
                continue
            dp[coin] = 1 # 1 coin to make it if there is this denomination
        
        for index, coin_count in enumerate(dp):
            
            min_coin_count = float('inf')

            for coin in coins:
                # look back to see if we have a previous way of making the required amount - coin
                look_back_index = index - coin
                if look_back_index >= 0 and dp[look_back_index] != -1:
                    min_coin_count = min(min_coin_count, dp[look_back_index] + 1)
            
            if min_coin_count != float('inf'):
                dp[index] = min_coin_count
            
        
        return dp[-1]


            
