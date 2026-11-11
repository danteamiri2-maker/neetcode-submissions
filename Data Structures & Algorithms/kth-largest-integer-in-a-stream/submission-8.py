import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)


    def add(self, val: int) -> int:
        if self.nums:
            i = 0
            while i < len(self.nums) and self.nums[i] <= val:
                i += 1
            self.nums.insert(i, val)
            print(self.nums)
            return self.nums[-self.k]
        else:
            self.nums.append(val)
            return val

        
