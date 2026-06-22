class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from heapq import heappush,heappop

        heap = []
        for i in arr:
            val = abs(i-x)
            heappush(heap,(val,i))
        
        return sorted([heappop(heap)[1] for i in range(k)])

        