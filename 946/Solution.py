class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        if not pushed and not popped:
            return True
        
        stack = []
        pushed = pushed[::-1]
        popped = popped[::-1]
        
        while True:
            
            stack.append(pushed.pop())
            
            while stack and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
            
            if not pushed:
                break
            
        
        return True if not stack else False
            
            
        
        
            
                
            
            
            
            
        