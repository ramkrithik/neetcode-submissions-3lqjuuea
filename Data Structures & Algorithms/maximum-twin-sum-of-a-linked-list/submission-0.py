# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_val = 0
        if not head:
            return max_val
        s = head
        f = head
        left_arr = []

        while f and f.next:
            left_arr = [s.val] + left_arr
            s = s.next
            f = f.next.next
        s2 = s

        while s2:
            max_val = max(max_val, s2.val + left_arr.pop(0))
            s2 = s2.next

        return max_val