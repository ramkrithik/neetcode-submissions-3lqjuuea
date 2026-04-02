class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited = set(num for num in nums if num>0)
        i=1
        while i in visited:
            i+=1
        return i

