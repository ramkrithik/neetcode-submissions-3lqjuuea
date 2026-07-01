# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q = []
        c = {}

        q.append((root,0))

        while q:

            for i in range(0,len(q)):
                node, shift = q.pop(0)
                if shift not in c:
                    c[shift] = []
                
                c[shift].append(node.val)
                if node.left:
                    q.append((node.left,shift-1))
                
                if node.right:
                    q.append((node.right,shift+1))
        print(c)
        return [c[k] for k in sorted(c.keys())]
