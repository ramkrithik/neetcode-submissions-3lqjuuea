class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total %k !=0:
            return False
        
        target = total//k

        nums.sort(reverse=True)

        bucket = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if bucket[j] + nums[i] <= target:
                    bucket[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    bucket[j] -= nums[i]

                    if bucket[j] == 0:
                        break

            return False     

        return backtrack(0)       
        