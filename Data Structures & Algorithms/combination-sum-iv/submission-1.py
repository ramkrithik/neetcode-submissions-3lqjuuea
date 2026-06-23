class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        target_dp = [0] * (target+1)
        target_dp[0] = 1

        for i in range(1,target+1):
            for j in nums:
                if j<=i:
                    target_dp[i] += target_dp[i-j]
        
        return target_dp[target]