# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node):
            if node is None:
                return True
            
            isLeft = dfs(node.left)
            isRight = dfs(node.right)

            if isLeft and isRight:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
            
                self.count += 1
                return True
            
            return False
        
        dfs(root)
        return self.count



        