class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        curr_sum = 0

        # loop through each element in nums
        for n in nums:
            # if curr_sum < 0, just takes away from sum so set to 0
            curr_sum = max(curr_sum, 0)

            curr_sum += n

            # assign max_sum to new max
            max_sum = max(curr_sum, max_sum)

        return max_sum