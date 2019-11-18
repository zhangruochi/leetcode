class Solution:
    def minSwap(self, A: List[int], B: List[int]):
        keep = [float("inf")] * len(A)
        swap = [float("inf")] * len(A)
        
        keep[0] = 0
        swap[0] = 1
        
        for i in range(len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1
            
            if A[i] > B[i-1] and B[i] > A[i-1]:
                keep[i] = min(keep[i],swap[i-1])
                swap[i] = min(keep[i-1]+1,swap[i])
        

        return min(keep[-1],swap[-1])
        