class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        from collections import deque
        q = deque()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))

        def bfs(q):
            time = 0
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()

                    if grid[r][c] == 1:
                        grid[r][c]=2

                    directions = [(1,0),(-1,0),(0,1),(0,-1)]

                    for dr,dc in directions:
                        if min(c+dc, r+dr) <0 or c+dc>=cols or r+dr>=rows or (r+dr,c+dc) in visited or grid[r+dr][c+dc] in [2,0]:
                            continue
                        q.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))
                time+=1
            return max(time - 1, 0)
        
        time = bfs(q)
        for row in grid:
            if 1 in row:
                return -1
        return time