class Solution:
    def numDecodings(self, s: str) -> int:

        c = {}

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            if i in c:
                return c[i]
            
            count = dfs(i+1)

            if i+1<len(s) and int(s[i:i+2])<=26:
                count += dfs(i+2)
            
            c[i] = count
            return c[i]
    
        return dfs(0)
        