class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        c = {}

        def dfs(i, capacity):
            if (i,capacity) in c:
                return c[(i,capacity)]
            if i == len(profit):
                return 0
            
            c[(i,capacity)] = dfs(i+1,capacity)
            max_profit = c[(i,capacity)]

            new_capacity = capacity - weight[i]

            if new_capacity >= 0:
                p = profit[i] + dfs(i+1,new_capacity)
                max_profit = max(max_profit,p)
                c[(i,capacity)] = max_profit
            
            return max_profit
        
        return dfs(0,capacity)