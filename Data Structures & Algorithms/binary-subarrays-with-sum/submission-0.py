class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def atmost(k):
            if k<0:
                return 0
            l = 0
            cursum = 0
            count = 0
            for r in range(len(nums)):
                cursum += nums[r]
                while cursum>k:
                    cursum -= nums[l]
                    l+=1
                
                count += (r-l)+1
            
            return count
        
        return atmost(goal) - atmost(goal-1)

        