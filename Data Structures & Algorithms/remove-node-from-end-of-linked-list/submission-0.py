# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        node = head
        l = 0
        while node:
            node = node.next
            l+=1
        
        to_remove_index = l-n
        
        if to_remove_index == 0:
            head = head.next
            return head
        
        node = head

        for i in range(0,to_remove_index-1):
            node = node.next
        
        node.next = node.next.next

        return head


        