class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        max_profit_grid = [[0]*(capacity+1) for i in range(len(weight))]
        
        for i in range(len(weight)):
            max_profit_grid[i][0] = 0
        
        for i in range(1,capacity+1):
            if weight[0]<=i:
                max_profit_grid[0][i] = profit[0]
        
        for i in range(1,len(weight)):
            for j in range(1,capacity+1):
                skip_cause_more_profit_previously = max_profit_grid[i-1][j]
                am_i_getting_more_profit = 0
                if j - weight[i] >=0:
                    am_i_getting_more_profit = profit[i] + max_profit_grid[i-1][j-weight[i]]
                max_profit_grid[i][j] = max(skip_cause_more_profit_previously,am_i_getting_more_profit)
        
        return max_profit_grid[-1][capacity]


        # Memoization
        # c = {}

        # def dfs(i, capacity):
        #     if (i,capacity) in c:
        #         return c[(i,capacity)]
        #     if i == len(profit):
        #         return 0
            
        #     c[(i,capacity)] = dfs(i+1,capacity)
        #     max_profit = c[(i,capacity)]

        #     new_capacity = capacity - weight[i]

        #     if new_capacity >= 0:
        #         p = profit[i] + dfs(i+1,new_capacity)
        #         max_profit = max(max_profit,p)
        #         c[(i,capacity)] = max_profit
            
        #     return max_profit
        
        # return dfs(0,capacity)