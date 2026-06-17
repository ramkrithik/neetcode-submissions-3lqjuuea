class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        from heapq import heappop, heappush

        minheap = [(grid[0][0],(0,0))]

        grid_movement = [(1,0),(0,1),(-1,0),(0,-1)]
        best = {}

        while minheap:
            time, coordinates = heappop(minheap)
            if coordinates in best:
                continue
            
            best[coordinates] = time

            for i,j in grid_movement:
                if min(coordinates[0] + i, coordinates[1]+j) < 0 or coordinates[0]+i >= len(grid) or coordinates[1]+j >= len(grid[0]):
                    continue
                new_coor = (coordinates[0] + i,coordinates[1]+j)
                if new_coor not in best:
                    heappush(minheap, (max(time, grid[new_coor[0]][new_coor[1]]),new_coor))
        
        return best[(len(grid)-1, len(grid[0])-1)]

            

