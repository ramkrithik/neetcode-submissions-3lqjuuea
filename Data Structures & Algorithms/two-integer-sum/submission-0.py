class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        balance_dict = {}
        for _, num in enumerate(nums):
            remaining = target - num
            if num in balance_dict:
                return [balance_dict[num], _]
            else:
                balance_dict[remaining] = _
        