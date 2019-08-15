class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return path
        stack = []
        for char in path.split("/"):
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        
        
        res = "/"+"/".join(stack) 
        return res