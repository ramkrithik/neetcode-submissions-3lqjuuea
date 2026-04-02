class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        k = int(len(nums)/3)
        elements = []
        for num in nums:
            count[num] = count.get(num,0) + 1
            if count[num] > k:
                if num not in elements:
                    elements.append(num)
        return elements

        