class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2)
                stack.append(n1)
                stack.append(n1+n2)
            elif op == "C":
                stack.pop()
            elif op == "D":
                n = stack.pop()
                stack.append(n)
                stack.append(n*2)
            else:
                stack.append(int(op))
            print(stack)
        
        return sum(stack)
        