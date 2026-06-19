class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        visited = {}
        num_ways = 0
        def dfs(i,curSum):
            nonlocal num_ways
            if i == len(nums):
                if curSum == target:
                    num_ways += 1
                return
            
            if (i,curSum) in visited:
                num_ways += visited[(i,curSum)]
                return
            
            oldways = num_ways
            dfs(i+1, curSum + nums[i])
            dfs(i+1, curSum - nums[i])
            visited[(i, curSum)] = num_ways - oldways

        dfs(0,0)
        return num_ways

