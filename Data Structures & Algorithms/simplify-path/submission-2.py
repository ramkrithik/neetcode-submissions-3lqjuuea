class Solution:
    def simplifyPath(self, path: str) -> str:

        path+= "/"
        stack = []
        working_path = ""
        dirs = []

        for i in path:
            if not stack:
                stack.append(i)
                working_path = "/"
                dirs = ["/"]
                continue
            
            if stack[-1] == "/" and i == "/":
                continue
            
            elif stack[-1] != "." and i=="/":
                new_dir = ""
                while stack and stack[-1] != "/":
                    new_dir += stack.pop()
                dirs.append(new_dir[::-1])
                working_path = dirs[-1]
            
            elif stack[-1] == "." and i == "/":
                dots = ""
                while stack and stack[-1] != "/":
                    dots += stack.pop()
                if dots == ".":
                    continue
                elif dots == "..":
                    dirs.pop()
                else:
                    dirs.append(dots[::-1])
                
                if not dirs:
                    dirs.append("/")
                working_path = dirs[-1]
            else:
                stack.append(i)
        
        if stack:
            new_dir = ""
            while stack and stack[-1] != "/":
                new_dir += stack.pop()
            dirs.append(new_dir[::-1])
        
        dirs = [di for di in dirs if di!= ""]
        dirs.pop(0)
        return f"/{"/".join(dirs)}"
                    

