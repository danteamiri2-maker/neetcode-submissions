class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res= []
        nums.sort()

        def backtrack(i, sol, total):
            if total == target:
                res.append(sol[:])
                return
            
            for j in range(i, len(nums)):
                if total + nums[i] <= target:
                    sol.append(nums[j])
                    backtrack(j, sol, total + nums[j])
                    sol.pop()

        backtrack(0, [], 0)
        return res
        
