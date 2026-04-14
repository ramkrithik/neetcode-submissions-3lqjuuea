class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c,visited):
            if min(r,c)<0 or r>=rows or c>=cols or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            grid[r][c] = 0
            count = 1

            count += dfs(r+1,c,visited)
            count += dfs(r-1,c,visited)
            count += dfs(r,c+1,visited)
            count += dfs(r,c-1,visited)

            return count
        
        island_size = [0]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    island_size.append(dfs(i,j,set()))
        return max(island_size)

        


        