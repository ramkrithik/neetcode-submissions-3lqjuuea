class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        from heapq import heappush, heappop

        adj = {}

        for u,v,t in times:
            if u not in adj:
                adj[u] = []
            
            adj[u].append((t,v))
        
        minheap = [(0,k)]
        best = {}

        while minheap:
            time,node = heappop(minheap)
            if node in best:
                continue
            best[node] = time

            if node in adj:
                for t,neigh in adj[node]:
                    if neigh not in best:
                        heappush(minheap,(t+time,neigh))
        
        return max(best.values()) if len(best) == n else -1
