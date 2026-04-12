class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math

        heap = []
        heapq.heapify(heap)

        for point in points:

            x = point[0] ** 2
            y = point[1] ** 2
            dist = math.sqrt(x+y)
            heapq.heappush(heap, (dist, point))
        
        if not heap:
            return []
        
        return [heapq.heappop(heap)[1] for i in range(k)]