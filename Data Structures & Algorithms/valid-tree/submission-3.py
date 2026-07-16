class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {}

        for edge in edges:
            e1, e2 = min(edge), max(edge)
            adj[e1] = adj.get(e1,[])
            adj[e1].append(e2)
            adj[e2] = adj.get(e2, [])
            adj[e2].append(e1)
        
        visited = set()
        def dfs(node,parent):
            if node in visited:
                return False
            
            visited.add(node)

            for neigh in adj.get(node,[]):
                if neigh == parent:
                    continue
                if not dfs(neigh,node):
                    return False
            
            return True
        
        return dfs(0,-1) and len(visited) == n