class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        from heapq import heappush, heappop

        minheap = [(0,(0,0))]
        best = {}

        movements = [(1,0),(0,1),(-1,0),(0,-1)]
        while minheap:
            effort, coord = heappop(minheap)
            if coord in best:
                continue
            
            best[coord] = effort

            for movement in movements:
                new_coord = (coord[0] + movement[0], coord[1] + movement[1])

                if new_coord[0] < 0 or new_coord[1] < 0 or new_coord[0] >= len(heights) or new_coord[1] >= len(heights[0]):
                    continue
                
                if new_coord not in best:
                    new_effort = abs(heights[new_coord[0]][new_coord[1]] - heights[coord[0]][coord[1]])
                    heappush(minheap, (max(effort, new_effort),new_coord))
            
        return best[(len(heights)-1, len(heights[0])-1)]
                
            
