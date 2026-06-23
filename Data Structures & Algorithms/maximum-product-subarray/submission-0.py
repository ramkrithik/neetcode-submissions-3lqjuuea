class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp_min = [0] * len(nums)


        for i in range(0,len(nums)):
            if i == 0:
                dp[i] = nums[i]
                dp_min[i] = nums[i]

            else:
                dp[i] = max(dp[i-1]*nums[i],dp_min[i-1]*nums[i],nums[i])
                dp_min[i] = min(dp[i-1]*nums[i],dp_min[i-1]*nums[i],nums[i])


        return max(dp)      