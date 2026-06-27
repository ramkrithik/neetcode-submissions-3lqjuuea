# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        node = head
        l = 0
        while node:
            l+=1
            node = node.next
        
        mid_point = l//2

        node = head
        for i in range(0,mid_point):
            node = node.next
        second = node.next
        node.next = None
        
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first = head
        while first and prev:
            tmp = first.next
            tmp2 = prev.next
            first.next = prev
            prev.next = tmp
            prev = tmp2
            first = tmp
            