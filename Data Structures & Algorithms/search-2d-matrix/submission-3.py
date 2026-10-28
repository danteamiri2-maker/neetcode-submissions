class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        


        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i]) - 1

            if len(matrix[i]) == 1:
                if matrix[i][0] == target:
                    return True

            while l < r:
                m = l + (r - l + 1)//2

                if matrix[i][m] == target or matrix[i][l] == target or matrix[i][r] == target:
                    return True
                
                if matrix[i][m] < target:
                    l = m + 1
                
                if matrix[i][m] >= target:
                    r = m - 1

        return False
        