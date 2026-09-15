class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.flip(matrix)

    

    def transpose(self, matrix) -> None:
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def flip(self, matrix) -> None:
        for row in matrix:
            left = 0
            right = len(matrix[0]) - 1

            while left < right:
                row[left], row[right] = row[right], row[left]
                left+=1
                right-=1

        