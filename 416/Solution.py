
"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        target = _sum // 2
        
        
        ## dp[i] 表示原数组是否可以取出若干个数字，其和为i
        dp = [False] * (target+1)
        dp[0] = True
        
        
        for num in nums:
            ## [num, target]
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i - num]
                print("num={}, i={}, dp={}".format(num,i,dp))
            print("")
        return dp[-1]