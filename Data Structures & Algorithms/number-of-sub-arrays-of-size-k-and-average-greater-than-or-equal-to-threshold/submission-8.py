class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        num_subarrays = 0
        
        l = 0
        r = k
        while r <= len(arr):
            # calculate average
            sub = [arr[i] for i in range(l, r)]
            avg = sum(sub) / k
            if avg >= threshold:
                num_subarrays += 1
            
            r += 1
            l += 1
            
        return num_subarrays