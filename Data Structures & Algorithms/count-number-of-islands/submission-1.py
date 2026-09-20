class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        for i in range(ROWS * COLS):
            r = i // COLS
            c = i % COLS

            if grid[r][c] == '0':
                continue
            
            islands+=1
            dfs(r, c)
        
        return islands


        