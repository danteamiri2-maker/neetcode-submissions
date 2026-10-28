class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = 0


        for l in range(len(prices)):
            r = len(prices) - 1
            while l < r:
                largest = max(largest, prices[r] - prices[l])
                r -= 1

        return largest