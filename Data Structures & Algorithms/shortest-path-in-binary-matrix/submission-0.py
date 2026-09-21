class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        queue = deque()
        visted = set()

        queue.append((0,0))
        visted.add((0,0))

        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                
                    if (min(new_r, new_c) < 0 
                    or new_r == ROWS 
                    or new_c == COLS 
                    or (new_r, new_c) in visted 
                    or grid[new_r][new_c] == 1):
                        continue
                    queue.append((new_r, new_c))
                    visted.add((new_r, new_c))
            length+=1
        
        return -1


                



        