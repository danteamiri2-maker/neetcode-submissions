class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        
        i = j = 0
        while j < len(nums):
            nums[i] = nums[j]
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            i += 1

        return i
            
        
        
