class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums_set = set(nums)
        # find the "start" of each subsequence

        # starts are where num - 1 does NOT appear
        starts = []
        for num in nums:
            if num - 1 not in nums_set:
                starts.append(num)

        # now see each of the starts
        longest = 0
        for start in starts:
            current_longest = 0
            # see how far you can go
            while start + current_longest in nums_set:
                current_longest += 1
            if current_longest > longest:
                longest = current_longest

        
        return longest