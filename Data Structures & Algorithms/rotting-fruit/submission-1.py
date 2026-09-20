class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        queue = deque()    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while fresh > 0 and queue:
            length = len(queue)
            for i in range(length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    new_r, new_c = dr + r, dc + c
                    if 0 <= min(new_r, new_c) and new_r < ROWS and new_c < COLS and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        fresh -= 1
                        
            time +=1
        
        return time if fresh == 0 else -1









        