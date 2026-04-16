class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            adj[j].append(i)
        
        visited = set()

        def dfs(node, visited):
            if node in visited:
                return False
            if adj[node] == []:
                return True
            
            visited.add(node)
            for near in adj[node]:
                if not dfs(near,visited):
                    return False
            visited.remove(node)
            adj[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i,visited):
                return False
        return True