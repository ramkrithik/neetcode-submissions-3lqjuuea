class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[-1]

        def dfs(i, end, c):
            if i>end:
                return 0
            
            if i in c:
                return c[i]
            
            c[i] = max(dfs(i+1,end,c), nums[i] + dfs(i+2,end,c))
            return c[i]

        return max(dfs(0,n-2,{}),dfs(1,n-1,{}))
