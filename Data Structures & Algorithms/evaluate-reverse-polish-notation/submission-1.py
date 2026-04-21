class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token in "+/-*":
                num2 = stack.pop()
                num1 = stack.pop()
                try:
                    val = int(eval(f"{num1}{token}{num2}"))
                except:
                    val = 0
                stack.append(val)
            else:
                stack.append(int(token))
        
        return stack[-1]
            

        