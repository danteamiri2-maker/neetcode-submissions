class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        '''
        # my first solution
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
        '''


        # Two binary searches
        # find row
        top = 0
        bottom = len(matrix)-1

        while top <= bottom:
            i = (bottom + top)//2

            if target > matrix[i][-1]:
                top = i + 1
            elif target < matrix[i][0]:
                bottom = i - 1
            else:
                break
            
        if top > bottom:
            return False

        print(i)
        
        # find column
        l = 0
        r = len(matrix[0])-1
        while l <= r:
            m = (r + l)//2

            if matrix[i][m] == target or matrix[i][l] == target or matrix[i][r] == target:
                return True
            
            if matrix[i][m] < target:
                l = m + 1
            
            if matrix[i][m] >= target:
                r = m - 1

        return False
        