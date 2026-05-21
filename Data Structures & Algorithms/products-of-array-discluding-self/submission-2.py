class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [nums[0]]
        for num_index in range(1, len(nums)):
            prefixes.append(prefixes[-1] * nums[num_index])
        
        suffixes = [0] * len(nums)
        suffixes[-1] = nums[-1]
        for num_index in range(len(nums) - 2, -1, -1):
            suffixes[num_index] = suffixes[num_index + 1] * nums[num_index]
        
        returned = [0] * len(nums)
        returned[0] = suffixes[1]
        returned[-1] = prefixes[-2]

        for i in range(1, len(returned) - 1):
            returned[i] = prefixes[i - 1] * suffixes[i + 1]

        return returned