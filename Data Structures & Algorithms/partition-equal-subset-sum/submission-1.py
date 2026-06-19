class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2 !=0:
            return False

        curr_elements = []
        visited = {}
        found = False
        target = sum(nums)//2
        def dfs(i, curSum, curr_elements):
            nonlocal found
            
            if curSum == target:
                found = True
            if i==len(nums) or curSum>target or found:
                return curSum, curr_elements
            if (i,curSum) in visited:
                return curSum,visited[(i,curSum)]
            
            dfs(i+1, curSum, curr_elements)
            dfs(i+1, curSum+nums[i], curr_elements+[nums[i]])
            visited[(i, curSum)] = curr_elements
            return curSum, curr_elements
        
        dfs(0,0,curr_elements)
        
        return found