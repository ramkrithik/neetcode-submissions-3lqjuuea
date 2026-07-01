class Solution:
    def numSquares(self, n: int) -> int:
        import sys
        sys.setrecursionlimit(100000)

        c = {}

        def dfs(remaining):
            if remaining  == 0:
                return 0
            
            if remaining in c:
                return c[remaining]
            
            res = float('inf')
            i =1

            while i*i <=remaining:
                res = min(res, 1+dfs(remaining - i*i))
                i+=1
            
            c[remaining] = res

            return c[remaining]
        
        return dfs(n)