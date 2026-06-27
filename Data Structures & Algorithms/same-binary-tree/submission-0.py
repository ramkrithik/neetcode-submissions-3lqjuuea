# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q:
            return False

        stack_p = [p]         
        stack_q = [q]

        while stack_p and stack_q:
            p_node = stack_p.pop()
            q_node = stack_q.pop()  

            if p_node.val != q_node.val:
                return False
            
            if p_node.left and q_node.left:
                stack_p.append(p_node.left)
                stack_q.append(q_node.left)
            elif p_node.left or q_node.left:
                return False
            
            if p_node.right and q_node.right:
                stack_p.append(p_node.right)
                stack_q.append(q_node.right)
            elif p_node.right or q_node.right:
                return False
        
        return len(stack_p) == len(stack_q)

                 
