"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        c = {None: None}

        new_head = Node(head.val)
        c[head] = new_head
        node = head.next

        while node:
            copy_node = Node(node.val)
            c[node] = copy_node
            node = node.next


        node = head
        while node:
            c[node].next = c[node.next]
            c[node].random = c[node.random]
            node = node.next
        
        return new_head
