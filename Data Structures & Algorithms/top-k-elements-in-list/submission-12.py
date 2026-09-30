import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            if num in counter:
                counter[num] += 1
            if num not in counter:
                counter[num] = 1
        
        
        
        topk = []
        for key, val in counter.items():
            topk.append([val, key])
        topk.sort()

        result = []
        while len(result) < k:
             result.append(topk.pop()[1])

        return result