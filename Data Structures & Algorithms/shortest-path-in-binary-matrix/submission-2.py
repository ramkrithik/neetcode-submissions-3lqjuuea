class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = [(0,0)]
        visited = set()
        visited.add((0,0))
        if grid[0][0] == 1:
            return -1
        def bfs(queue):
            length = 1
            while q:
                for i in range(len(q)):
                    r,c = q.pop(0)
                    if r==rows-1 and c == cols-1:
                        return length

                    directions = [(1,0),(-1,0),(0,1),(0,-1),
                    (1,-1),(-1,-1),(-1,1),(1,1)]

                    for dr,dc in directions:
                        if min(r+dr, c+dc)<0 or r+dr >=rows or c+dc>= cols or grid[r+dr][c+dc] == 1 or ((r+dr,c+dc) in visited):
                            continue
                        q.append(((r+dr),(c+dc)))
                        visited.add((r+dr,c+dc))
                length +=1
            return -1
        
        return bfs(q)
                
