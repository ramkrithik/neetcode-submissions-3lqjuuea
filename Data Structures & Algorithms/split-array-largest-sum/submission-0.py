class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def isValid(max_sum):
            cur_sum = 0
            count = 1
            for i in nums:
                cur_sum += i
                if cur_sum > max_sum:
                    count += 1
                    cur_sum = i
                
                if count>k:
                    return False
                
            return True
        
        l = max(nums)
        r = sum(nums)

        found = r
        

        while l<r:
            m = l+(r-l)//2

            valid = isValid(m)

            if valid:
                r = m
                found = r
            else:
                l = m+1
        
        return found

                
                
            