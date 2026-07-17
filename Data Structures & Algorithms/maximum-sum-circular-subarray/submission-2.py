class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = 0
        max_sum = nums[0]
        cur_max = 0
        min_sum = nums[0]
        cur_min = 0

        for num in nums:
            total+=num
            cur_max = max(cur_max+num, num)
            max_sum = max(max_sum,cur_max)

            cur_min = min(cur_min+num,num)
            min_sum = min(cur_min, min_sum)
        
        if total == min_sum:
            return max_sum

        return max(max_sum, total-min_sum)
