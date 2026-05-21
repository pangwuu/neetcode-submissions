import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = []
        heapq.heapify(k_largest)
        for num in nums:
            if len(k_largest) < k:
                heapq.heappush(k_largest, num)
                continue
            
            # compare the current lowest one to the new num. add the larger one
            current_k_largest = heapq.heappop(k_largest)

            if num > current_k_largest:
                heapq.heappush(k_largest, num)
            else:
                heapq.heappush(k_largest, current_k_largest)
        
        return heapq.heappop(k_largest)
