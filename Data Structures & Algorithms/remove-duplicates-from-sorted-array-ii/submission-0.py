class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        


        l = 0
        for num in nums:
            '''
                Condition 1: lets the first two elements of nums stay where they are, increments write index l
                Condition 2: if current number is different from number two back in nums, write num to write index l and increment l
            '''
            if l < 2 or num != nums[l-2]:
                nums[l] = num
                l += 1
        return l
        