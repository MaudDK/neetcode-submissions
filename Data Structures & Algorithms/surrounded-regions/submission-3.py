class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        
        #Add all edges to a queue
        for i in range(ROWS):
            if board[i][0] == 'O':
                board[i][0] = 'T'
                q.append((i, 0))

            if board[i][COLS - 1] == 'O':
                board[i][COLS - 1] = 'T'
                q.append((i, COLS - 1))

        for i in range(COLS):
            if board[0][i] == 'O':
                board[0][i] = 'T'
                q.append((0, i))
            
            if board[ROWS - 1][i] == 'O':
                board[ROWS - 1][i] = 'T'
                q.append((ROWS - 1, i))
        
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        #BFS
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr , nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or board[nr][nc] != 'O':
                    continue

                board[nr][nc] = 'T'
                q.append((nr, nc))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                if board[i][j] == 'T':
                    board[i][j] = 'O'

        







        
                



        