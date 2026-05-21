class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        maps = {}
        for index, num in enumerate(nums):
            # check if the missing piece is inside
            missing = target - num
            if missing in maps:
                # maps[num] = index
                smaller = min(index, maps[missing])
                larger = max(index, maps[missing])
                return [smaller, larger]    

            maps[num] = index 
