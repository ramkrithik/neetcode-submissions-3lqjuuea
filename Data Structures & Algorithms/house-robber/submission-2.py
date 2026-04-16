class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        max_at_val = [0] * len(nums)

        max_at_val[0] = nums[0]
        max_at_val[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            max_at_val[i] = max(max_at_val[i-1], max_at_val[i-2] + nums[i])
        
        
        return max(max_at_val[-1],max_at_val[-2])