import heapq

class Point:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.distance = self.x ** 2 + self.y ** 2
        self.negative_distance = -self.distance

    def __lt__(self, other):
        return self.negative_distance < other.negative_distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closest = [] # queue is based off the negative distance stat of the point

        heapq.heapify(k_closest)

        for point in points:
            newPoint = Point(point)

            if len(k_closest) < k:
                heapq.heappush(k_closest, newPoint)
                continue
            
            # if it is now k points large, we do a comparison
            kth_furthest = heapq.heappop(k_closest)

            if kth_furthest.distance < newPoint.distance:
                # then we just put this back onto the heap, and newpoint is too large to make it
                heapq.heappush(k_closest, kth_furthest)
                continue
            else:
                heapq.heappush(k_closest, newPoint)
        
        return [[point.x, point.y] for point in k_closest]





