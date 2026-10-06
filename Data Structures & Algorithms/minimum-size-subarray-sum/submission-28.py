class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        curr_sum = 0
        l = 0
        res = float("inf")

        if sum(nums) < target:
            return 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                # remove values from left to compensate for adding larger number
                res = min(res, r - l + 1)
                curr_sum -= nums[l]
                l += 1
            
        return res