class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1

        if l == r and nums[0] == target:
            return 0
        
        while l < r:
            m = l + (r - l + 1) // 2
            if nums[m] == target:
                return m
            
            if nums[l] == target:
                return l
            
            if nums[r] == target:
                return r
            
            if nums[m] < target:
                l = m+1
            
            if nums[m] >= target:
                r = m-1
            
        return -1 