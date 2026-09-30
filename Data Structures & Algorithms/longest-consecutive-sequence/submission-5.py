class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_length = 0
        unique_nums = set(nums)
        for num in unique_nums:
            if num-1 not in unique_nums:
                length = 1
                while num+1 in unique_nums:
                    length += 1
                    num += 1
                max_length = max(length, max_length)
        
        return max_length


        
        
        

            
                