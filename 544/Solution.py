class Solution:
    def findContestMatch(self, n: int) -> str:
        if not n:
            return ""
            
        def helper(x):
            if len(x) == 2:
                return "(" + x[0] + "," + x[1] + ")"
            
            return helper( ["(" + x[i] + "," + x[len(x)-1-i] + ")" for i in range(len(x)//2)] )
    
        return helper([str(i) for i in range(1,n+1)])