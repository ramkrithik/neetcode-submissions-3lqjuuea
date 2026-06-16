class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0,nums)    
    
    def helper(self, i, nums):
        if i == len(nums):
            return [[]]
        
        all_perms = []
        perms = self.helper(i+1,nums)

        for p in perms:
            for j in range(len(p)+1):
                curPerm = p.copy()
                curPerm.insert(j,nums[i])
                all_perms.append(curPerm)
        return all_perms
