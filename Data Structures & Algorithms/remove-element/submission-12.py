class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        tmp = []
        for n in nums:
            if n != val:
                tmp.append(n)
                k += 1
        
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        
        return k