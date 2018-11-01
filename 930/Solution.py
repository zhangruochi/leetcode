"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

 

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.

"""


class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        prefix_sum,cum = [0],0
        for num in A:
            cum += num
            prefix_sum.append(cum)
        
        table,count = {},0
        for sum_ in prefix_sum:
            count += table.get(sum_-S,0)
            if sum_ not in table:
                table[sum_] = 1
            else:
                table[sum_] += 1
        return count
