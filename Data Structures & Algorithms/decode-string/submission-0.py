class Solution:
    def decodeString(self, s: str) -> str:
        
        stack =[]
        int_stack = []
        for i in s:
            if i == "[":
                integer = ""
                while stack and stack[-1].isnumeric():
                    integer=stack.pop()+integer
                stack.append(i)
                if integer == "":
                    integer = "1"
                
                int_stack.append(int(integer))
            
            elif i == "]":
                chars = ""
                while stack and stack[-1]!="[":
                    chars = stack.pop()+chars
                
                # last bracket off
                stack.pop()

                m_factor = int_stack.pop()

                stack.append(m_factor*chars)
            
            else:
                stack.append(i)            

        return "".join(stack)
        