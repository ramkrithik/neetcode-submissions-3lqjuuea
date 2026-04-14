class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c,visited):
            if min(r,c)<0 or r>=rows or c>=cols or grid[r][c] == "0":
                return
            
            visited.add((r,c))
            
            grid[r][c] = "0"
            
            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)
        islands = 0
        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == "1":
                    dfs(i,j,set())
                    islands+=1
        return islands


        