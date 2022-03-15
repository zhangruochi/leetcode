class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    
        
        return dp[-1]



class Solution:
    def rob(self, nums: List[int]) -> int:

        # f(k) = max(f(k-1), f(k-2) + nums[k])

        # f(0) = 0
        # f(1) = nums[1]

        if not nums:
            return 0


        dp = [-1] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        
        return dp[-1]
