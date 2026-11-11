import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)
        while len(stones) > 1:
            big, small = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if big == small:
                pass
            else:
                heapq.heappush_max(stones, big - small)
        
        if len(stones) == 1:
            return stones[0]
        
        return 0
        