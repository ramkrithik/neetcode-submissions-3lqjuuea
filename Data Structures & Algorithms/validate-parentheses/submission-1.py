class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}":"{",")":"(","]":"["}
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            elif not stack or stack.pop() != mapping[i]:
                return False
        return len(stack) == 0
            

        