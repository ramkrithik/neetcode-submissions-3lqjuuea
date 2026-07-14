# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop

        heap = []
        i=0
        for h in lists:
            node = h
            while node:
                heappush(heap, (node.val,i,node))
                i+=1
                node = node.next
        
        if not heap:
            return None
        val,idx,head = heappop(heap)
        head.next = None

        node = head

        while heap:
            val,idx,new_node = heappop(heap)
            new_node.next = None
            node.next = new_node
            node = node.next
        
        return head
