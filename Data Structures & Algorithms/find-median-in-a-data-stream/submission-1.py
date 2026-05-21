import heapq

class MedianFinder:

    def __init__(self):
        self.topHalf = [] # min heap
        self.lowHalf = [] # max heap
        
        heapq.heapify(self.topHalf)
        
        heapq.heapify(self.lowHalf)

        # use this to track if we have to rebalance the sides each time
        self.size = 0

    def addNum(self, num: int) -> None:
        # size of either side cannot exceed the other side by > 1. 
        
        # add to the smaller half
        if self.lowHalf:
            top_of_bottom = -self.lowHalf[0]
        else:
            top_of_bottom = float('-inf')
        
        if self.topHalf:
            bottom_of_top = self.topHalf[0]
        else:
            bottom_of_top = float('inf')

        # 2 cases
        if num > top_of_bottom:
            # add to top half
            heapq.heappush(self.topHalf, num)
        elif num <= top_of_bottom:
            # add to bottom
            heapq.heappush(self.lowHalf, -num)

        def rebalanceHalves():

            while len(self.lowHalf) > len(self.topHalf) + 1:
                # continuously pop the top element from low half and push it to the top half
                top_of_bottom = -heapq.heappop(self.lowHalf)
                heapq.heappush(self.topHalf, top_of_bottom)
            
            while len(self.topHalf) > len(self.lowHalf) + 1:
                bottom_of_top = -heapq.heappop(self.topHalf)
                heapq.heappush(self.lowHalf, bottom_of_top)
        
        rebalanceHalves()
        self.size += 1
        

    def findMedian(self) -> float:
        # empty halves? return the other one
        
        if not self.topHalf:
            return -self.lowHalf[0]
        if not self.lowHalf:
            return self.topHalf[0]
        
        if self.size % 2 == 0:
            # return average of both
            top_of_bottom = -self.lowHalf[0]
            bottom_of_top = self.topHalf[0]
            return (top_of_bottom + bottom_of_top) / 2
        else:
            # which side is bigger?
            if len(self.topHalf) > len(self.lowHalf):
                return self.topHalf[0]
            elif len(self.lowHalf) > len(self.topHalf):
                return -self.lowHalf[0]

        

        

        
        