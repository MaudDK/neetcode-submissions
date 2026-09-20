class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        clickedColor = image[sr][sc]

        if clickedColor == color:
            return image

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or image[r][c] != clickedColor:
                #Out of bounds
                return
            
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
            
        