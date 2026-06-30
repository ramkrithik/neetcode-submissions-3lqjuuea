# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        c = {}
        
        def dfs(curr, iteration):
            if not curr:
                return False
            
            if not curr.left and not curr.right:
                if iteration not in c:
                    c[iteration] = []
                c[iteration].append(curr.val)
                return True
            
            if curr.left:
                is_leaf = dfs(curr.left, iteration)
                if is_leaf:
                    curr.left = None
            if curr.right:
                is_leaf = dfs(curr.right,iteration)
                if is_leaf:
                    curr.right = None
            
            return False
        
        i = 0
        while root:
            if dfs(root, i):
                break
            i+=1

        return list(c.values())