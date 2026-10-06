class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        num_subarrays = 0
        window = []
        l = 0
        r = 0
        while r <= len(arr):
            
            if len(window) == k:
                avg = sum(window) / k
                if avg >= threshold:
                    num_subarrays += 1

                if r < len(arr):
                    window.pop(0)
                    window.append(arr[r])

            if len(window) < k:
                window.append(arr[r])

            r += 1
            
        return num_subarrays