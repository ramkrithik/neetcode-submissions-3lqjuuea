class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        from collections import Counter
        h = Counter(nums)
        max_num = -1
        for k,v in h.items():
            if v == 1:
                max_num = max(max_num,k)
        
        return max_num
        