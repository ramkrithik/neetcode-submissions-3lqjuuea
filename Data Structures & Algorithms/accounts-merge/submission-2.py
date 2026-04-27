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
    
    def union(self,x,y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind()
        email_to_name = {}

        for name, *emails in accounts:
            for email in emails:
                email_to_name[email] = name
                uf.union(email,emails[0])
        
        groups = {}

        for email in email_to_name:
            parent = uf.find(email)
            if parent not in groups:
                groups[parent] = []
            
            groups[parent].append(email)
        
        return [[email_to_name[email]] + groups[email] for email in groups]
