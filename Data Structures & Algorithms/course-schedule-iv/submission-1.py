class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = {i:[] for i in range(numCourses)}

        for i in prerequisites:
            adj[i[0]].append(i[1])
        
        reachable = {i: set() for i in range(numCourses)}
        def dfs(node):
            if reachable[node]:
                return reachable[node]
            for nei in adj[node]:
                reachable[node].add(nei)
                reachable[node].update(dfs(nei))
            return reachable[node]

        for i in range(numCourses):
            dfs(i)

        return [v in reachable[u] for u, v in queries]
        