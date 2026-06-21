class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        matrix = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if i==0 and j ==0:
                    matrix[i][j] = grid[i][j]
                elif i-1 < 0:
                    matrix[i][j] = matrix[i][j-1] + grid[i][j]
                elif j-1 < 0:
                    matrix[i][j] = matrix[i-1][j] + grid[i][j]
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + grid[i][j]
        
        return matrix[-1][-1]
        