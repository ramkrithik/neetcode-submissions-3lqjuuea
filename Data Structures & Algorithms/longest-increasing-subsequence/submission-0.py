class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        c = {}
        def dfs(i, prev):
            if i>=len(nums):
                return 0
            
            if (i,prev) in c:
                return c[(i,prev)]
            skip = dfs(i+1,prev)
            take = 0
            if prev == -1 or nums[i]>nums[prev]:
                take += 1+dfs(i+1,i)
            
            c[(i,prev)] =  max(skip,take)
            return c[(i,prev)]
        
        return dfs(0,-1)
        

        