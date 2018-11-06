class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        cum,res = 1,[]
        for num in nums:
            res.append(cum)
            cum = cum * num
        cum,cur = 1,len(nums)-1
        while cur >= 0:
            res[cur] *= cum
            cum = cum * nums[cur]
            cur -= 1
        return res