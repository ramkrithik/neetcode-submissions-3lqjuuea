class UF:
    def __init__(self):
        self.parent = {}
    
    def find(self, point):
       self.parent.setdefault(point, point)
       while point != self.parent[point]:
           self.parent[point] = self.parent[self.parent[point]]
           point = self.parent[point]
       return point
    
    def union(self,point1, point2):
        point1, point2 = tuple(point1),tuple(point2)
        parent1,parent2 = self.find(point1), self.find(point2)
        if parent1 == parent2:
            return False
        self.parent[self.find(point1)] = self.find(point2)
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def calc_dist(point1, point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
        
        from heapq import heappush, heappop

        min_heap = []

        for i in range(0,len(points)):
            for j in range(i+1,len(points)):
                d = calc_dist(points[i],points[j])
                heappush(min_heap,(d,[points[i],points[j]]))
        
        uf = UF()
        mst = []
        dist = 0

        while len(mst)<len(points)-1:
            d,edge = heappop(min_heap)
            if not uf.union(edge[0],edge[1]):
                continue
            
            mst.append(edge)
            dist += d
        
        return dist







        # Prim's

        # visited = set()

        # visited.add(tuple(points[0]))
        # total_dist = 0
        # minheap = []

        # for point in points[1:]:
        #     dist = calc_dist(points[0],point)
        #     heappush(minheap,(dist,tuple(point)))
        
        # while minheap:
        #     if len(visited) == len(points):
        #         break
            
        #     dist, dest_point = heappop(minheap)
        #     if tuple(dest_point) in visited:
        #         continue
        #     total_dist += dist
        #     visited.add(tuple(dest_point))

        #     for point in points:
        #         if tuple(point) not in visited:
        #             d = calc_dist(dest_point,point)
        #             heappush(minheap,(d,tuple(point)))
                
        # return total_dist