class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S: return 0
        
        dp1 = [0]
        
        if S[0] == "0":
            dp1.append(0)
        else:
            dp1.append(1)
            
        for i in range(1,len(S)):
            if S[i] == "1":
                dp1.append(dp1[-1]+1)
            else:
                dp1.append(dp1[-1])
        
        dp1.append(0)
        
        dp2 = [0]
        
        if S[-1] == "1":
            dp2.append(0)
        else:
            dp2.append(1)
        
        for i in range(len(S)-2,-1,-1):
            if S[i] == "0":
                dp2.append(dp2[-1]+1)
            else:
                dp2.append(dp2[-1])
        dp2.append(0)
        dp2.reverse()
        
        min_ = float("inf")
        for i in range(1,len(S)+1):

            min_ = min(min_,dp1[i-1]+dp2[i+1])
            
        return min_