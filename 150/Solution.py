class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {"+","-","*","/"}
        for t in tokens:
            if t not in operator:
                stack.append(int(t))
            else:
                s = stack.pop()
                f = stack.pop()
                
                if t == "+":
                    stack.append(f+s)
                elif t == "-":
                    stack.append(f-s)
                elif t == "*":
                    stack.append(f*s)
                elif t == "/":               
                    stack.append(int(f/s))
            
        return stack[-1]
                
                
                
        
            