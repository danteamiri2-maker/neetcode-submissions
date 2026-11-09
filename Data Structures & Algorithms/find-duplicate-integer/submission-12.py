class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force
        """
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
        """

        # hash set
        """
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        """


        


        for n in nums:
            # mark n as seen by making it's index negative
            # can do this since len(nums) == max(nums) + 1
            # so abs(n) - 1 is guaranteed to be a valid index of nums

            idx = abs(n) - 1
            if nums[idx] < 0:
                # n has already been seen
                return abs(n)
            
            # if n hasnt been seen, mark it as seen 
            nums[idx] *= -1
        return -1


        