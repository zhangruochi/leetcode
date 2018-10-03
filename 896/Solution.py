"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""



class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(1,len(A)):
            if A[i] < A[i-1]:
                for j in range(1, len(A)):
                    if [j] > A[j-1]:
                        return False

        return True

    # 时空复杂度都高    
    def isMonotonic2(self, A):  
        if len(A) == 1:
            return True
        B = sorted(A)
        if B == A or B == A[::-1]:
            return True

        return False  

    
    def isMonotonic3(self,A):
        inc,dec = False,False
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                inc = True
            if A[i] < A[i-1]:
                dec = True

        return not inc or not dec            




                
            
            
            

       