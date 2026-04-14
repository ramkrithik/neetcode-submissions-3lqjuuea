class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if min(r,c)<0 or r>=rows or c >=cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        islands = 0
        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands+=1
        return islands


        