class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        stack = []
        start = 0
        for i in range(len(S)):
            if S[i] == ")":
                start = stack.pop()
            else:
                stack.append(i)
            
            if not stack:
                res += S[start+1:i]
        
        return res
                