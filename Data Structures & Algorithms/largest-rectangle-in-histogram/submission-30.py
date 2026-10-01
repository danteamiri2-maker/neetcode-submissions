class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        stack = []
        left_wall = [-1]*n 
        for i in range(n):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                left_wall[i] = stack[-1]
            stack.append(i)

        stack = []
        right_wall = [n]*n 
        for i in range(n-1, -1, -1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right_wall[i] = stack[-1]
            stack.append(i)        
        
        max_area = 0
        for i in range(n):
            left_wall[i] += 1
            right_wall[i] -= 1
            area = heights[i] * (right_wall[i] - left_wall[i] + 1)
            max_area = max(max_area, area)
        return max_area
                
            
