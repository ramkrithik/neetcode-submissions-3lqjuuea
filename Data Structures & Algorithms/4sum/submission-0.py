class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = set()

        for idx1, t1 in enumerate(nums):

            triplets = set()
            for j in range(idx1+1, len(nums)):
                t2 = nums[j]
                remaining = target - t2 - t1

                l = j+1
                r = len(nums)-1

                while l<r:
                    s = nums[l] + nums[r]

                    if s > remaining:
                        r -=1
                    elif s < remaining:
                        l += 1
                    else:
                        triplets.add((t2,nums[l],nums[r]))
                        l +=1
                        r-=1
            
            for triplet in triplets:
                quads.add(tuple(sorted(triplet + (t1,))))
            
        return [list(i) for i in quads]