class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_pos = {}
        for _, num in enumerate(nums):
            unique_pos[num] = unique_pos.get(num,[]) + [_]
        for _,key in enumerate(unique_pos.keys()):
            nums[_] = key
        return len(unique_pos.keys())
        