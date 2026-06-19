class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for req in prerequisites:
            adj[req[1]].append(req[0])
        
        topSort = []
        visited = set()

        def dfs(node, visited, path):
            if node in path:
                return False
            
            if node in visited:
                return True
            
            visited.add(node)
            path.add(node)

            for i in adj[node]:
                if not dfs(i,visited,path):
                    return False
            path.remove(node)
            topSort.append(node)
            return True
        
        for i in adj:
            path = set()
            
            if not dfs(i,visited,path):
                return []
        
        return topSort[::-1]
        