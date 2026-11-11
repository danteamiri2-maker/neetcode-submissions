from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = lambda x, y: sqrt(x**2 + y**2)

        k_points = []
        while points:
            x, y = points.pop()
            z = -dist(x, y)
            if len(k_points) >= k:
                heapq.heappushpop(k_points, (z, x, y))
            else:
                heapq.heappush(k_points, (z, x, y))
        
        return [[x, y] for _, x, y in k_points]
