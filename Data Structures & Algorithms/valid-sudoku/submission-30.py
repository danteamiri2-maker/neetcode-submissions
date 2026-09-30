class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isNumber(s):
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            if s in numbers:
                return True
            return False

        def containsDuplicates(arr):
            numbers = [a for a in arr if isNumber(a)]
            if len(set(numbers)) == len(numbers):
                return False
            return True
        
        def validBlock(block):
            r, c = 3, 3
            return not containsDuplicates([block[i][j] for i in range(r) for j in range(c)])
        
        def validCol(col):
            return not containsDuplicates(col)

        def validRow(row):
            return not containsDuplicates(row)

        
        
        
        r = 0
        valid_row = True
        while r < 9 and valid_row:
            arr = board[r]
            valid_row = validRow(arr)
            r += 1
        
        if not valid_row:
            return False
        
        c = 0
        valid_col = True
        while c < 9 and valid_col:
            arr = [0] * 9
            for i in range(9):
                arr[i] = board[i][c]
            valid_col = validCol(arr)
            c += 1

        if not valid_col:
            return False

        centers = [[1, 1], [1, 4], [1, 7],
                    [4, 1], [4, 4], [4, 7], 
                    [7, 1], [7, 4], [7, 7]]
        
        b = 0
        valid_block = True
        while b < 9 and valid_block:
            r, c = centers[b]
            block = [temp[c-1:c+2] for temp in board[r-1:r+2]]
            print(block)
            valid_block = validBlock(block)
            b += 1
        
        if not valid_block:
            return False
        
        return True

            


            