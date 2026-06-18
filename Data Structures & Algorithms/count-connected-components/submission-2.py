class UnionFind:
    def __init__(self):
        self.parent = {}
        
    def find(self, n):
        self.parent.setdefault(n,n)
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self,n1,n2):
        p1, p2 =self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        self.parent[self.find(p1)] = self.find(p2)
        
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()
        res = n
        for edge in edges:
            if uf.union(edge[0],edge[1]):
                res-=1

        return res
        