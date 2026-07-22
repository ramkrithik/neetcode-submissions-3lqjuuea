class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []

        out = ""

        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                s = ""
                while stack and stack[-1] != "(":
                    s = stack.pop() + s
                
                if stack and stack[-1] == "(":
                    s = stack.pop()+s+i
                
                stack.append(s)
            else:
                stack.append(i)
        
        for i in stack:
            if i == "(" or i == ")":
                continue
            else:
                out+=i

        return out

                

        