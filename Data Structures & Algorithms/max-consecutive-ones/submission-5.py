class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        base_count = 0
        max_count = 0
        for i in range(0,len(nums)):
            if nums[i] == 1 and (nums[i-1] == 1 or i==0):
                base_count+=1
                max_count = max(base_count, max_count)
            elif nums[i]==1:
                base_count=1
                max_count = max(base_count, max_count)
        return max_count
        