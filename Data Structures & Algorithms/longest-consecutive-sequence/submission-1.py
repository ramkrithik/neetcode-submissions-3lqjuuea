class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count=0
        for num in num_set:
            count = 1
            for _ in range(len(nums)):
                if num-1 not in num_set:
                    break
                count+=1
                num-=1
            max_count = max(max_count,count)
        return max_count
            

        