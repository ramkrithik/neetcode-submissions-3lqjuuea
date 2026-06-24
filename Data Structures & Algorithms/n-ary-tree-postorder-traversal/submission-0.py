"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        visit = [False]
        val = []
        while stack:
            curr, visited = stack.pop(),visit.pop()

            if visited:
                val.append(curr.val)
            
            else:
                stack.append(curr)
                visit.append(True)
                for child in curr.children[::-1]:
                    if child:
                        stack.append(child)
                        visit.append(False)
        
        return val