class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(nums, target):

            l = 0
            r = len(nums)-1
            while l <= r:
                m = (r + l)//2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
            return -1
        
        
        if nums[0] < nums[-1]:
            return binarySearch(nums, target)

        elif nums[0] > nums[-1]:

            #i = 0
            #while nums[i] != max(nums):
            #    i += 1

            l = 0
            r = len(nums)-1
            while l < r:
                m = (r + l)//2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            i = l-1
            left = nums[:i+1]
            right = nums[i+1:]

            # is in left section:
            if left[0] <= target and left[-1] >= target:
                return binarySearch(left, target)
                
            if right[0] <= target and right[-1] >= target:
                j = binarySearch(right, target)
                if j != -1:
                    return len(left) + binarySearch(right, target)
                else:
                    return -1
            
        elif nums[0] == nums[-1] == target:
            return 0
        
        return -1

