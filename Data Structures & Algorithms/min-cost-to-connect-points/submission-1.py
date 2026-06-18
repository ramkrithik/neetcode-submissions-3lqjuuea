class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def calc_dist(point1, point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
        
        from heapq import heappush, heappop

        visited = set()

        visited.add(tuple(points[0]))
        total_dist = 0
        minheap = []

        for point in points[1:]:
            dist = calc_dist(points[0],point)
            heappush(minheap,(dist,tuple(point)))
        
        while minheap:
            if len(visited) == len(points):
                break
            
            dist, dest_point = heappop(minheap)
            if tuple(dest_point) in visited:
                continue
            total_dist += dist
            visited.add(tuple(dest_point))

            for point in points:
                if tuple(point) not in visited:
                    d = calc_dist(dest_point,point)
                    heappush(minheap,(d,tuple(point)))
                
        return total_dist