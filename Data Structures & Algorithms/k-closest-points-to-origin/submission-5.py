import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        heapq._heapify_max(closest_points)

        for point in points:
            distance = -(point[0] ** 2) - (point[1] ** 2)

            heapq.heappush(closest_points, [distance, point])

            if len(closest_points) > k:
                heapq.heappop(closest_points)

        return [closest_point[1] for closest_point in closest_points]