class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        cum_sum = [0]
        sum_ = 0
        for num in nums:
            sum_ += num
            cum_sum.append(sum_)
        
        
        pre_min = cum_sum[0]
        res = -float("inf")
                
        for sum_ in cum_sum[1:]:
            if sum_ - pre_min > res:
                res = sum_ - pre_min
            
            if sum_ < pre_min:
                pre_min = sum_
        
        return res
                

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        sum_ = 0
        pre_min = 0
        res = -float("inf")
        
        for num in nums:
            sum_ += num
            
            if sum_ - pre_min > res:
                res = sum_ - pre_min
            
            if sum_ < pre_min:
                pre_min = sum_
        
        return res
                

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur_max = 0
        res = -float("inf")

        for num in nums:
            cur_max = max(cur_max + num, num)
            res = max(cur_max, res)
            
        return res
        
        