class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_run = 0
        l, r = 0, 0
        run = 0
        while r < len(nums):
            if nums[r] == 1:
                run += 1
                r += 1
            else:
                l = r
                r = r + 1
                run = 0
            longest_run = max(longest_run, run)
        return longest_run

