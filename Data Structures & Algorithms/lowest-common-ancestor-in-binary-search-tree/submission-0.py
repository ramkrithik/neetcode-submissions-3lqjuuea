# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if min(p.val, q.val) < root.val and max(p.val, q.val) > root.val:
            return root
        
        stack = [root]

        while stack:
            
            curr = stack.pop()

            if min(p.val, q.val) <= curr.val and max(p.val, q.val) >= curr.val:
                return curr
            
            if p.val < curr.val and q.val < curr.val:
                stack.append(curr.left)
            if p.val > curr.val and q.val > curr.val:
                stack.append(curr.right)
        
        return root
