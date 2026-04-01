class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Pref: (1,1) (2,1) (4,2) (6,8)
        # Suffix: (1,48) (2,24) (4,6) (6,1)
        # (48) (24) (12) (8)
        # Pref: (5,1) (2,5) (3,10) (4,30)
        # Suffix: (5,24) (2,12) (3,4) (4,1)
        # (120) (60) (40) (30)

        left_array = [1]
        for i in range(1,len(nums)):
            left_array.append(left_array[-1] * nums[i-1])
        right_array = [1]
        for i in range(len(nums)-2,-1,-1):
            right_array = [nums[i+1] * right_array[0]] + right_array
        return [a*b for a,b in zip(left_array, right_array)]