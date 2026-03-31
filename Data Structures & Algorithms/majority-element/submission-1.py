class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counter = {}
        # max_count = 0
        # max_count_element = nums[0]
        # for num in nums:
        #     if num not in counter:
        #         counter[num] = 0
        #     counter[num] += 1
        #     if counter[num] > max_count:
        #         max_count_element = num
        #         max_count = counter[num]
        # return max_count_element
        
        # ---- Boyer-Moore Voting Algorithm ----
        # always the candidate surives, its like apocalype, kill count until you
        # find survivor
        candidate, count = nums[0], 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
        