# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def _inorder(root):
            if not root:
                return
            
            _inorder(root.left)
            values.append(root.val)
            _inorder(root.right)
        
        _inorder(root)
        return values[k-1]
        