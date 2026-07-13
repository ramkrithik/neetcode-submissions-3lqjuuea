# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 and l2:
            return None

        h1 = l1
        s1 = ""
        while h1:
            s1 = f"{h1.val}" + s1
            h1=h1.next
        h2 = l2
        s2 = ""
        while h2:
            s2 = f"{h2.val}" + s2
            h2=h2.next
        
        if s1 == "":
            s1 = 0
        
        if s2 == "":
            s2 = 0
        s1,s2 = int(s1),int(s2)
        out = str(s1+s2)[::-1]

        head = ListNode(int(out[0]),None)
        itr = head
        for i in range(1,len(out)):
            itr.next = ListNode(int(out[i]),None)
            itr = itr.next
        
        return head
            


        