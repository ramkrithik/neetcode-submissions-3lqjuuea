class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        cur_comb, all_comb = [], []
        self.helper(0,cur_comb,all_comb,0,target,nums)
        return all_comb
        

    def helper(self,i,curr_comb,all_comb,curSum,target,nums):
        if curSum == target:
            all_comb.append(curr_comb.copy())
            return
        if i>=len(nums) or curSum > target:
            return
        
        curr_comb.append(nums[i])
        curSum += nums[i]
        self.helper(i,curr_comb,all_comb,curSum,target,nums)
        sub = curr_comb.pop()
        curSum -= sub
        self.helper(i+1,curr_comb,all_comb,curSum,target,nums)