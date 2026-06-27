# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_len = 0

        def dfs(node):

            nonlocal max_len

            if not node:
                return 0
            
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            max_len = max(max_len, left_len + right_len)

            return max(left_len, right_len) + 1
        
        dfs(root)

        return max_len

        