from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        returned_nums = set()
        counter = defaultdict(int)
        threshold = int(len(nums) / 3)

        for num in nums:
            counter[num] += 1
            if counter[num] > threshold:
                returned_nums.add(num)
        
        return list(returned_nums)
