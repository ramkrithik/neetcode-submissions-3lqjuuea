class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        from collections import deque
        prefix = deque()
        postfix = deque()

        for i in nums:
            if not prefix:
                prefix.append(i)
            else:
                prev=prefix[-1]
                prefix.append(prev+i)
        
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            if not postfix:
                postfix.appendleft(num)
            else:
                prev = postfix[0]
                postfix.appendleft(prev+num)

        for i in range(len(prefix)):
            if prefix[i] == postfix[i]:
                return i
        return -1