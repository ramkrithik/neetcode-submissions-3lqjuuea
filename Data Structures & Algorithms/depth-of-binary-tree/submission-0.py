# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [(root,1)]
        max_height = 1

        while stack:
            node, height = stack.pop()
            max_height = max(max_height,height)
            if node.left:
                stack.append((node.left,height+1))
            if node.right:
                stack.append((node.right,height+1))
        
        return max_height
        