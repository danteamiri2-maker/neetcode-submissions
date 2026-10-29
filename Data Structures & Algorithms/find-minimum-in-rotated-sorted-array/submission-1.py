class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if nums[l] > nums[r]:
            while l <= r:
                m = l + (r - l + 1)//2
                if nums[m] > nums[r]:
                    l = m
                elif nums[m] < nums[r]:
                    r = m
                else:
                    return nums[m]
        else:
            return nums[l]
            
        