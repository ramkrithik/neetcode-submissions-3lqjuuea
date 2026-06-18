class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def _construct_mst(new_edges,forced_edge = None):
            from heapq import heappop, heappush

            adj = {}

            for a,b,w in new_edges:
                if a not in adj:
                    adj[a] = []
                if b not in adj:
                    adj[b] = []
                
                adj[a].append((w,b))
                adj[b].append((w,a))
            
            visited = set()
            minheap = []
            totalCost = 0

            if forced_edge:
                a,b,w  = forced_edge
                visited.add(a)
                visited.add(b)
                totalCost = w
                for i in adj[a]:
                    heappush(minheap,i)
                for i in adj[b]:
                    heappush(minheap,i)
            else:
                if not new_edges:
                    return -1
                start = new_edges[0][0]
                visited.add(start)
                for i in adj[start]:
                    heappush(minheap, i)
                    
            while minheap:
                if len(visited) == n:
                    return totalCost
                
                w,node = heappop(minheap)
                if node in visited:
                    continue
                
                totalCost += w
                visited.add(node)

                for i in adj[node]:
                    if i[1] not in visited:
                        heappush(minheap,i)
            return totalCost if len(visited) == n else -1
        
        original_cost = _construct_mst(edges)

        critical = []
        pseudo = []

        for idx,edge in enumerate(edges):
            new_edges = edges[:idx] + edges[idx+1:]
            cost = _construct_mst(new_edges)
            if cost == -1 or cost > original_cost:
                critical.append(idx)
            else:
                cost = _construct_mst(new_edges,edges[idx])
                if cost == original_cost:
                    pseudo.append(idx)

        return [critical,pseudo] 
            

                
