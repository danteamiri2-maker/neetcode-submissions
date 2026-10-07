class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        biggest = [-1]*len(arr)
        curr_max = -float("inf")
        for l in range(len(arr) - 2, -1, -1):
            curr_max = max(curr_max, arr[l + 1])
            biggest[l] = curr_max
        
        return biggest
