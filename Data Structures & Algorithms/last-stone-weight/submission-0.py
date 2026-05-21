import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        new_stones = []
        for stone in stones:
            new_stones.append(-stone)
        
        heapq.heapify(new_stones)

        while len(new_stones) > 1:
            heavier = heapq.heappop(new_stones)
            lighter = heapq.heappop(new_stones)
            
            if heavier == lighter:
                continue
            else:
                new_stone_weight = heavier - lighter
                
                heapq.heappush(new_stones,new_stone_weight)
        

        if not new_stones:
            return 0
        
        # pop last element
        return -heapq.heappop(new_stones)