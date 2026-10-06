class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        def kadanes_max_subarray(nums):
            max_sum = nums[0]
            curr_sum = 0

            for i in range(len(nums)):
                j = i % len(nums)
                n = nums[j]
                curr_sum = max(curr_sum, 0)
                curr_sum += n
                max_sum = max(curr_sum, max_sum)
            
            return max_sum
        

        # two cases: wrapping subarray and non_wrapping subarray
        if nums and [n for n in nums if n > 0]:
            total = sum(nums)
            max_sum = kadanes_max_subarray(nums)
            min_sum = -kadanes_max_subarray([-n for n in nums])
            return max(max_sum, total - min_sum)
        if nums and [n for n in nums if n <= 0]:
            return max(nums)