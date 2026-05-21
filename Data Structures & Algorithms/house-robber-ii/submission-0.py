class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        # rob first but not last
        opt_1 = [0] * (len(nums) - 1)
        opt_1[0] = nums[0]
        opt_1[1] = max(nums[0], nums[1])

        for i, num in enumerate(nums):
            if i == len(nums) - 1 or i < 2:
                continue
            
            # ensure you don't rob both houses
            opt_1[i] = max(opt_1[i - 1], opt_1[i - 2] + nums[i])
        
        max_1 = opt_1[-1]


        # rob not the first but include the last
        opt_2 = [0] * len(nums)
        opt_2[0] = -100
        opt_2[1] = nums[1]
        opt_2[2] = max(nums[1], nums[2])

        for i, num in enumerate(nums):
            if i <= 2:
                continue
            
            # ensure you don't rob both houses
            opt_2[i] = max(opt_2[i - 1], opt_2[i - 2] + nums[i])
        
        max_2 = opt_2[-1]

        return max(max_1, max_2)

