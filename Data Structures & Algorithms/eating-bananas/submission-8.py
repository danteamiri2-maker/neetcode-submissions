class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def hours_needed(piles, k):
            h = 0
            for i in range(len(piles)):
                h += piles[i] // k
                if piles[i] % k > 0:
                    h += 1
            return h


        low = 1
        high = max(piles)
        k = high
        while low <= high:
            mid = (high + low) // 2
            h_curr = hours_needed(piles, mid)
            print(mid, h_curr)
            if h_curr <= h:
                k = min(k, mid)
                high = mid - 1
            elif h_curr > h:
                low = mid + 1
            
        return k

