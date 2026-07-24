class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l = 0
        res = 0
        curr_flip = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                curr_flip += 1
            
            while l<=r and curr_flip>k:
                if nums[l] == 0:
                    curr_flip -= 1
                l+=1
            
            res = max(res, r-l+1)
        
        return res
        