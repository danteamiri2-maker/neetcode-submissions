class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # create a hash map of frequencies
        res = []
        freq = defaultdict(int)
        curr = []
        A = [] # unique numbers in candidates

        for num in candidates:
            if freq[num] == 0:
                A.append(num)
            freq[num] += 1

        
    
        def backtrack(nums, target, curr, i):
            if target == 0:
                res.append(curr[:])
                return 

            if target < 0 or i >= len(nums):
                return 


            if freq[nums[i]] > 0:
                curr.append(nums[i])
                freq[nums[i]] -= 1
                backtrack(nums, target - nums[i], curr, i)
                freq[nums[i]] += 1
                curr.pop()

            backtrack(nums, target, curr, i+1)
                

        backtrack(A, target, curr, 0)
        return res