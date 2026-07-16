class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        c = {}
        def dfs(l,r):

            if l>r:
                return 0
            
            if (l,r) in c:
                return c[(l,r)]
            
            c[(l,r)] = 0

            for i in range(l,r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]

                coins+= dfs(l,i-1) + dfs(i+1,r)
                
                c[(l,r)] = max(c[(l,r)], coins)

            return c[(l,r)]
        
        return dfs(1,len(nums)-2)
        