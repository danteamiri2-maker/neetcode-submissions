class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        leftMax = heights[l]
        rightMax = heights[r]
        area = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, heights[l])
                area += leftMax - heights[l]
            else:
                r -= 1
                rightMax = max(rightMax, heights[r])
                area += rightMax - heights[r]
        print(area)
    
        return area
