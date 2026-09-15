class Solution:
    def spiralOrder(self, matrix: List[List]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        y = 0
        x = 0

        dy = 0 # -> 1 -> 0.  dy, = dx
        dx = 1 # -> 0 -> -1.  dx = -dy

        res = []
        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "." 

            if not 0 <= y + dy < rows or not 0 <= x + dx < cols or matrix[y+dy][x+dx] == ".":
                dy, dx = dx, -dy
            
            y+=dy
            x+=dx
        
        return res