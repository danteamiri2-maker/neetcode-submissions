class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        num_subarrays = 0
        window = []
        l = 0
        r = 0
        curr_sum = 0
        while r <= len(arr):
            
            if len(window) == k:
                if curr_sum >= threshold * k:
                    num_subarrays += 1

                if r < len(arr):
                    val = window.pop(0)
                    window.append(arr[r])
                    curr_sum += arr[r]
                    curr_sum -= val


            if len(window) < k:
                curr_sum += arr[r]
                window.append(arr[r])

            r += 1
            
        return num_subarrays