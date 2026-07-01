# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_len = 1

        def dfs(node,curr_len):
            nonlocal max_len
            if not node:
                return 
            
            max_len = max(max_len,curr_len)

            if node.left:
                if node.left.val == node.val+1:
                    dfs(node.left, curr_len+1)
                else:
                    dfs(node.left,1)

            if node.right:
                if node.right.val == node.val+1:
                    dfs(node.right, curr_len+1)
                else:
                    dfs(node.right, 1)
        
        dfs(root,1)
        return max_len
                
