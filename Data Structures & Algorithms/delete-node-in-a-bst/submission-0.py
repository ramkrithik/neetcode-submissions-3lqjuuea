# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minval(node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr
        
        def remove(root,val):
            if not root:
                return None
            
            if root.val < val:
                root.right = remove(root.right,val)
            elif root.val > val:
                root.left = remove(root.left,val)
            else:

                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min_value = minval(root.right)
                    root.val = min_value.val
                    root.right = remove(root.right,min_value.val)
            return root
        
        return remove(root,key)