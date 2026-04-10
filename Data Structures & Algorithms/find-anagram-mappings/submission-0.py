class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pos = {}
        for _,num in enumerate(nums2):
            if num not in pos:
                pos[num] = []
            pos[num].append(_)
        
        return [pos[num].pop(0) for num in nums1]
        