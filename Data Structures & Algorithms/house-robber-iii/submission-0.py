# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        c = {}
        def dfs(node,rob):
            if not node:
                return 0
            
            if (node,rob) in c:
                return c[(node,rob)]
            skip = dfs(node.left, True) + dfs(node.right, True)

            amount = 0
            if rob:
                amount = node.val + dfs(node.left, False) + dfs(node.right, False)
            c[(node,rob)] = max(skip, amount)
            return c[(node,rob)]
            
        return dfs(root, True)