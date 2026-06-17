class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        from heapq import heappush, heappop

        adj = {}

        for idx, coor in enumerate(edges):
            if coor[0] not in adj:
                adj[coor[0]] = []
            adj[coor[0]].append((succProb[idx],coor[1]))
            if coor[1] not in adj:
                adj[coor[1]] = []
            adj[coor[1]].append((succProb[idx],coor[0]))
        
        minheap = [(-1,start_node)]
        best = {}

        while minheap:

            prob, node = heappop(minheap)

            if node in best:
                continue
            
            best[node] = -1*prob

            if node in adj:
                for p, n in adj[node]:
                    if n not in best:
                        heappush(minheap, (prob*p,n))
        
        return 0.0 if end_node not in best else best[end_node]
                