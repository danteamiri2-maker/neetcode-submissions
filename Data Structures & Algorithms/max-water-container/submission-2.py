class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def bruteForce(heights):
            max_area = 0
            for l in range(len(heights)):
                for r in range(l, len(heights)-1):
                    height = min(heights[l], heights[r])
                    width = r - l
                    max_area = max(max_area, height * width)
            
            return max_area
        

        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            area = h * w
            max_area = max(max_area, area)

            #move smaller side
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area