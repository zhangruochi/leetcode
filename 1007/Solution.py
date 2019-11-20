class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        
        a,b = 0,0
        
        for i in range(n):
            if not (A[i] == A[0] or B[i] == A[0]):
                break
            
            if A[i] == A[0]:
                a += 1
            if B[i] == A[0]:
                b += 1
            
            if i == len(A)-1:
                return min(n-a,n-b)
            
        a,b = 0,0   
                    
        for i in range(n):
            if not (A[i] == B[0] or B[i] == B[0]):
                break
            
            if A[i] == B[0]:
                a += 1
            if B[i] == B[0]:
                b += 1
            
            if i == len(A)-1:
                return min(n-a,n-b)
        
        return -1
    
                
                