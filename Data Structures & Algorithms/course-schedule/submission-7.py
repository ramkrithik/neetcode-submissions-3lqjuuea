class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            adj[j].append(i)
        
        visited = set()

        def dfs(node, visited, path):
            if node in path:
                return False

            if node in visited:
                return True
            
            visited.add(node)
            path.add(node)
            for near in adj[node]:
                if not dfs(near,visited,path):
                    return False
            path.remove(node)
            return True

        for i in range(numCourses):
            path = set()
            if not dfs(i,visited, path):
                return False
        return True