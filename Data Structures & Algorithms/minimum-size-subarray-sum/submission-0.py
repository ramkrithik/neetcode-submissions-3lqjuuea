class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0
        min_len = float("inf")

        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                min_len = min(R-L+1, min_len)
                total = total-nums[L]
                L+=1
        
        return 0 if min_len == float("inf") else min_len