"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
 

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 

Note:

N is a positive integer and will not exceed 15.
"""


class Solution:
    def countArrangement(self, N: int) -> int:
        
        array = list(range(1,N+1))
        count = 0
        visited = set()
        
        

        def per(depth):
            nonlocal array, count, visited
            
            if depth == N+1:
                count += 1
                return 
            
            for num in array:
                if (not num in visited) and (num % depth == 0 or depth % num == 0):
                    visited.add(num)
                    per(depth+1)
                    visited.remove(num)
                    
        per(1)
        return count
            
                    
                
            
            
            
            
            
            
            
            
        