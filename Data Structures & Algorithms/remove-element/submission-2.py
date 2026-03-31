class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k+=1
        return k
        # try:
        #     for i in range(0,len(nums)):
        #         nums.remove(val)
        #     return len(nums)
        # except:
        #     return len(nums)
        