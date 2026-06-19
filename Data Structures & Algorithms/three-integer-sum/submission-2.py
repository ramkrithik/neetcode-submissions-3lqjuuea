class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = set()
        for idx, target in enumerate(nums):

            l = idx +1
            r = len(nums)-1

            updated = -1*target


            while l<r:
                s = nums[l] + nums[r]
                if s>updated:
                    r -=1
                elif s<updated:
                    l+=1
                else:
                    triplets.add((target,nums[l],nums[r]))
                    l+=1
                    r-=1
        
        return [list(i) for i in triplets]


        