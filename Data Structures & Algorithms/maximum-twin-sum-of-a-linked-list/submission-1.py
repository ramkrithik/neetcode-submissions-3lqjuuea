# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        from collections import deque
        max_val = 0
        if not head:
            return max_val
        s = head
        f = head
        left_arr = deque()

        while f and f.next:
            left_arr.appendleft(s.val)
            s = s.next
            f = f.next.next
        s2 = s

        while s2:
            max_val = max(max_val, s2.val + left_arr.popleft())
            s2 = s2.next

        return max_val