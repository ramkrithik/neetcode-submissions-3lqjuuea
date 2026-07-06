class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        l = 0
        window = []
        zero_count = 0
        max_len = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                window.append(nums[r])
                max_len = max(max_len, len(window))
            elif nums[r] == 0 and zero_count ==0:
                window.append(nums[r])
                zero_count += 1
                max_len = max(max_len, len(window))
            else:
                while l<r:
                    if nums[l] == 0:
                        window.pop(0)
                        zero_count -= 1
                        l+=1
                        break
                    else:
                        window.pop(0)
                        l+=1
                window.append(nums[r])
                zero_count += 1
                max_len = max(max_len, len(window))
                
        return max_len
            
            
            

