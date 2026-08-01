class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        missing = []
        if not nums:
            return [[lower,upper]]
        if nums[0] != lower:
            missing.append([lower,nums[0]-1])
        
        for i in range(0,len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                continue
            missing.append([nums[i]+1, nums[i+1]-1])
        
        if nums[-1] != upper:
            missing.append([nums[-1]+1,upper])
        
        return missing