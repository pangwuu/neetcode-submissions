class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # optimal[n] shows the optimal amount after the nth house
        optimal = [0] * len(nums)

        # base case
        optimal[0] = nums[0]
        optimal[1] = max(nums[0], nums[1])

        # Well opt[n] = opt[n-1] OR opt[n-2] + nums[n]
        for index, num in enumerate(optimal):
            if index <= 1:
                continue
            
            optimal[index] = max(optimal[index - 1], optimal[index - 2] + nums[index])
        
        return optimal[-1]