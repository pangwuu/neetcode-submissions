class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # longest = 0
        seen = set()
        starts = set()

        for num in nums:
            seen.add(num)
            if num - 1 not in seen:
                starts.add(num)
            if num - 1 in seen:
                if num in starts:
                    starts.remove(num)
        
        # now we look for the longest sequence
        longest = 0
        nums_set = set(nums)
        for start in starts:
            # just keep going until you stop!
            cursor = start
            while True:
                cursor += 1
                if cursor in nums_set:
                    continue
                else:
                    break
            # end element - first
            length = cursor - start
            if length > longest:
                longest = length
        
        return longest

            