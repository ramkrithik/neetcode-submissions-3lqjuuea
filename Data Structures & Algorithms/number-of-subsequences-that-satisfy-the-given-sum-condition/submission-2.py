class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:


        MOD = 10**9 + 7
        nums.sort()
        l = 0
        r = len(nums)-1
        res = 0
        while l<=r:
            if nums[l] + nums[r] <= target:
                res = (res + pow(2, r - l, MOD)) % MOD
                l +=1
            else:
                r-=1
        return res
        # res = [0]
        # def dfs(i,curr_array):
            
        #     if i >= len(nums):
        #         if curr_array and (curr_array[0] + curr_array[-1]) <= target:
        #             res[0] = (res[0] + 1) % MOD
        #         return
            
        #     dfs(i+1, curr_array)
        #     dfs(i+1,curr_array + [nums[i]])

        #     return
        
        # dfs(0,[])
        # return res[0]
            
            
        