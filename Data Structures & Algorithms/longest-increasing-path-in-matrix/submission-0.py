class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M,N = len(matrix[0]),len(matrix)
        movement = [(0,1),(1,0),(-1,0),(0,-1)]
        c = {}
        def dfs(i,j):
            if (i,j) in c:
                return c[(i,j)]

            best = 1
            for move in movement:
                ni, nj = i+move[0], j+move[1]
                
                if min(ni,nj)>=0 and ni<N and nj<M and matrix[ni][nj] > matrix[i][j]:
                    best = max(best,1+dfs(ni,nj))
            
            c[(i,j)] = best

            return c[(i,j)]
        
        return max(dfs(i,j) for i in range(N) for j in range(M))

