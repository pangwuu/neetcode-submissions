import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = sorted(nums, reverse=True)[:k]

        # kth largest = the minimum of the largest k numbers
        heapq.heapify(nums)
        self.stream = nums
        self.size = k

    def add(self, val: int) -> int:
        # check if the stream is empty
        if len(self.stream) == 0 or len(self.stream) < self.size:
            heapq.heappush(self.stream, val)
            return self.stream[0]
        
        # is the stream adequately sized?

        # check if the new added value is larger or smaller than the kth largest
        kth_largest = self.stream[0]
        if val < kth_largest:
            return kth_largest
        else:
            heapq.heappop(self.stream)
            heapq.heappush(self.stream, val)
            return self.stream[0]

        
