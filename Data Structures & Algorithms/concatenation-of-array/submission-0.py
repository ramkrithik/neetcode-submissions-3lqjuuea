class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) <= 0:
            return nums
        for i in range(0,len(nums)):
            nums.append(nums[i])
        return nums