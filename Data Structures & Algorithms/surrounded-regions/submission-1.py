class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        visted = set()
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def sinkIsland(r, c):
            canSink = True
            region = []

            q = deque()
            q.append((r, c))

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    if (r, c) in visted:
                        continue
                    
                    visted.add((r, c))
                    region.append((r, c))
                    
                    if min(r, c) == 0 or r == ROWS - 1 or c == COLS - 1:
                        canSink = False
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        
                        #Check out of bounds
                        if min(nr, nc) < 0 or nr == ROWS or nc == COLS or board[nr][nc] == 'X':
                            continue
                    
                        q.append((nr, nc))
            
            if canSink:
                for r, c in region:
                    board[r][c] = 'X'
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    sinkIsland(r, c)
                



        