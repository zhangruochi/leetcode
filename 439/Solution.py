class Solution:
    def parseTernary(self, expression: str) -> str:
        if not expression:
            return expression
        
        
        stack = []
        index = len(expression) - 1
        
        while index >= 0:
            if expression[index] == "?":
                index -= 1
                b = expression[index]
                
                f = stack.pop()
                _ = stack.pop()
                s = stack.pop()
                
                if b == "T":
                    stack.append(f)
                else:
                    stack.append(s)
                index -= 1
            else:
                stack.append(expression[index])
                index -= 1
        return stack[-1]
            
            