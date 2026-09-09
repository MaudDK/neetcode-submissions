class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows * cols) - 1

        while l <= r:
            m = l + (r - l) // 2

            i = m // cols
            j = m % cols

            if target == matrix[i][j]:
                return True
            
            if target < matrix[i][j]:
                r = m - 1
            else:
                l = m + 1
        
        return False
            


        