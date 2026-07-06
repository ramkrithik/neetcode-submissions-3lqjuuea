# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node):
            if not node:
                return 0,0
            inc,dec = 1,1
            if node.left:
                l_inc, l_dec = dfs(node.left)
                if node.left.val == node.val+1:
                    inc = max(inc,l_inc+1)
                elif node.left.val == node.val-1:
                    dec = max(dec,l_dec+1)

            if node.right:
                r_inc,r_dec = dfs(node.right)
                if node.right.val == node.val+1:
                    inc = max(inc,r_inc+1)
                elif node.right.val == node.val-1:
                    dec = max(dec,r_dec+1)
            
            self.max_len = max(self.max_len, inc + dec - 1)
            return inc, dec
        
        dfs(root)
        return self.max_len
        