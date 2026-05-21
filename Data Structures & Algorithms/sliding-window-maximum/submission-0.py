import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        neg_nums = [-num for num in nums]

        maxes = []
        l = 0
        for r in range(len(neg_nums) - k + 1):
            # make a heap
            window = neg_nums[r:r + k]

            heapq.heapify(window)
            # pop the heap
            maxes.append(- heapq.heappop(window))
        
        return maxes


            
            

            
        