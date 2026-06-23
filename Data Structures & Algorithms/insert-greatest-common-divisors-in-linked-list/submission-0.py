# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []

        curr_node = head
        while curr_node.next:
            next_node = curr_node.next

            from math import gcd

            comm = gcd(curr_node.val, next_node.val)
            gcd_node = ListNode(comm,next_node)
            curr_node.next=gcd_node
            curr_node = next_node

        return head        