class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        n = len(grid)
        m = len(grid[0])
        treasure = deque()
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == 0:
                    treasure.append((i,j))
        
        movements = [(0,1),(1,0),(0,-1),(-1,0)]

        for t in treasure:
            q = deque()
            q.append(t + (0,))
            visit = set()
            visit.add(t)
            while q:
                i,j,dist = q.popleft()
                if grid[i][j] != 0 and grid[i][j] != -1:
                    grid[i][j] = min(grid[i][j],dist)
                for move in movements:
                    new_i = i+move[0]
                    new_j = j+move[1]
                    if min(new_i, new_j)<0 or new_i >= n or new_j >= m or (new_i,new_j) in visit or grid[new_i][new_j] == -1:
                        continue
                    q.append((new_i,new_j,dist+1))
                    visit.add((new_i,new_j))
        