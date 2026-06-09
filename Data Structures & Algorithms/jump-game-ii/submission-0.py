class Solution:
    def jump(self, nums: List[int]) -> int:
        n= len(nums)
        res = 0
        l,r = 0,0

        while r < n-1:
            max_reach = 0
            for i in range(l,r+1):
                max_reach = max(max_reach, i + nums[i])
            
            l = r+1
            r = max_reach
            res += 1
        return res


