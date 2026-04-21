class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        matrix = [[0]*len(obstacleGrid[0]) for i in obstacleGrid]

        if obstacleGrid[0][0] == 1:
            return 0
        matrix[0][0]=1

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):

                if obstacleGrid[i][j] == 1 or (i==0 and j==0):
                    continue

                if i-1 <0:
                    matrix[i][j] += matrix[i][j-1]
                elif j-1<0:
                    matrix[i][j] += matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        return matrix[-1][-1]
