class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        for c, n in enumerate(nums):
            if n > 0:
                break
            if c > 0 and n == nums[c - 1]:
                continue

            
            l = c+1
            r = len(nums)-1
            while l < r:
                res = n + nums[l] + nums[r]
                if res == 0:
                    sol.append([nums[c], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                if res > 0:
                    r -= 1
                if res < 0:
                    l += 1
                
        return sol
        