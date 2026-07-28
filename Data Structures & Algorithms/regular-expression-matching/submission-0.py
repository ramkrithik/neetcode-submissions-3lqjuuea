class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)
        c={}
        def dfs(i,j):

            if (i,j) in c:
                return c[i,j]
            
            if j == m:
                return i==n
            
            first_match = i<n and (s[i] == p[j] or p[j] == ".")

            if j+1<m and p[j+1] == "*":
                ans = dfs(i,j+2) or (first_match and dfs(i+1,j))
            else:
                ans = first_match and dfs(i+1,j+1)
            
            c[(i,j)] = ans
            return ans
        
        return dfs(0,0)