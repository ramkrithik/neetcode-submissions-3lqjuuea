class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curset, subsets = [],[]
        self.helper(0,nums,curset,subsets)
        return subsets

    def helper(self, i, nums, curset, subsets):
        if i>=len(nums):
            subsets.append(curset.copy())
            return
        
        curset.append(nums[i])
        self.helper(i+1,nums,curset,subsets)
        curset.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i+=1
        self.helper(i+1,nums,curset,subsets)
