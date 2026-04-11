# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        
        def traverse(root,curr_sum):

            curr_sum += root.val

            if not root.left and not root.right:
                if curr_sum != targetSum:
                    return False
                else:
                    return True
            elif root.left and traverse(root.left,curr_sum):
                return True
            elif root.right and traverse(root.right,curr_sum):
                return True
            
            return False
        
        return traverse(root,0)
            