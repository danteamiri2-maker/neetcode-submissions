import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        if self.nums:
            if len(self.nums) < self.k:
                heapq.heappush(self.nums, val)
            else:
                heapq.heappushpop(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
        return heapq.nlargest(self.k, self.nums)[-1]
        
        
