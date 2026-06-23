class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        c = {}
        def dfs(i,buy):
            if i >= len(prices):
                return 0
            
            if (i,buy) in c:
                return c[(i,buy)]

            skip = dfs(i+1,buy)
            if buy:
                cur = dfs(i+1,0) - prices[i]
            else:
                cur = dfs(i+2,1)+ prices[i]
            
            c[(i,buy)] = max(skip, cur)
            return c[(i,buy)]
        
        return dfs(0,1)