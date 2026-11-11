import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        klargest = []

        while nums:
            n = nums.pop()
            if len(klargest) < k:
                heapq.heappush(klargest, n)
            else:
                heapq.heappushpop(klargest, n)
        
        return klargest[0]