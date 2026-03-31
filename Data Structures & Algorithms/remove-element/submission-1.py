class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            for i in range(0,len(nums)):
                nums.remove(val)
            return len(nums)
        except:
            return len(nums)
        