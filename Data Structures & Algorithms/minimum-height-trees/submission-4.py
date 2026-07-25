class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n<=2:
            return list(range(n))

        adj = {}

        for i in edges:
            adj[i[0]] = adj.get(i[0],[]) + [i[1]]
            adj[i[1]] = adj.get(i[1],[]) + [i[0]]

        degree = {i: len(adj[i]) for i in range(n)}
        
        leaves = deque([node for node in degree if degree[node] == 1])
        remaining = n

        while remaining>2:
            remaining -=len(leaves)
            next_l = []

            for leaf in leaves:
                for nb in adj[leaf]:
                    degree[nb] -=1
                    if degree[nb] == 1:
                        next_l.append(nb)
            leaves = deque(next_l)
        
        return list(leaves)

        
        # mht = {}

        # for i in adj.keys():
        #     q = [i]
        #     visit = set()
        #     visit.add(i)
        #     level = 1

        #     while q:

        #         for _ in range(len(q)):
        #             node = q.pop(0)
        #             for neigh in adj[node]:
        #                 if neigh in visit:
        #                     continue
                        
        #                 visit.add(neigh)
        #                 q.append(neigh)
        #         level += 1

        #     mht[level] = mht.get(level,[]) + [i]

        # min_h = min(mht.keys())
        # return mht[min_h]