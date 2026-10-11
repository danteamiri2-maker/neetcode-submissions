class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res, sol = [], []

        def backtrack(n):
            if n == len(nums):
                res.append(sol[:])
                return 
            
            sol.append(nums[n])
            backtrack(n + 1)
            sol.pop()

            backtrack(n + 1)

        backtrack(0)
        return res