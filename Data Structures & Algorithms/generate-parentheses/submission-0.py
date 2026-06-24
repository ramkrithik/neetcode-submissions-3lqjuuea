class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []

        def dfs(open_c,close_c):
            if open_c == close_c == n:
                res.append("".join(stack))
            
            if open_c < n:
                stack.append("(")
                dfs(open_c+1,close_c)
                stack.pop()
            
            if close_c<open_c:
                stack.append(")")
                dfs(open_c,close_c+1)
                stack.pop()
        
        dfs(0,0)
        return res

