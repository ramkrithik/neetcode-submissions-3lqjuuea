class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        c = {}
        def dfs(i,j,k):

            if k == len(s3):
                return True
            
            if (i,j) in c:
                return c[(i,j)]

            a = False
            if i < len(s1) and s1[i] == s3[k]:
                a = dfs(i+1,j,k+1)
            b = False
            if j<len(s2) and s2[j] == s3[k]:
                b = dfs(i,j+1,k+1)
            
            c[(i,j)] = a or b
            return c[(i,j)]
        
        return dfs(0,0,0)
