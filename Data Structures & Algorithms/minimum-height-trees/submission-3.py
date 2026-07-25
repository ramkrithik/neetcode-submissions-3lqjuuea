class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n<=2:
            return list(range(n))

        adj = {}

        for i in edges:
            adj[i[0]] = adj.get(i[0],[]) + [i[1]]
            adj[i[1]] = adj.get(i[1],[]) + [i[0]]

        
        mht = {}

        for i in adj.keys():
            q = [i]
            visit = set()
            visit.add(i)
            level = 1

            while q:

                for _ in range(len(q)):
                    node = q.pop(0)
                    for neigh in adj[node]:
                        if neigh in visit:
                            continue
                        
                        visit.add(neigh)
                        q.append(neigh)
                level += 1

            mht[level] = mht.get(level,[]) + [i]

        min_h = min(mht.keys())
        return mht[min_h]