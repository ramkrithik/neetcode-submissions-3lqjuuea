# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, root.val)]
        res = 0

        while stack:
            curr, max_val = stack.pop()

            if curr.val >= max_val:
                res += 1
            
            max_val = max(max_val,curr.val)

            if curr.left:
                stack.append((curr.left,max_val))
            
            if curr.right:
                stack.append((curr.right,max_val))
        
        return res

        