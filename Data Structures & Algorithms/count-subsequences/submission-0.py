class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        c = {}
        def dfs(i1,i2):
            if i2 == len(t):
                return 1
            
            if i1 == len(s):
                return 0
            if (i1,i2) in c:
                return c[(i1,i2)]
            count = dfs(i1+1,i2)
            if s[i1] == t[i2]:
                count+=dfs(i1+1,i2+1)
            
            c[(i1,i2)] = count
            
            return c[(i1,i2)]

        return dfs(0,0)



        