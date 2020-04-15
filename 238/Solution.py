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

from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        suffix_product = deque([1])
        

        for num in nums:
            prefix_product.append(prefix_product[-1] * num)
            
        for num in nums[::-1]:
            suffix_product.appendleft(suffix_product[0] * num)
            
            
        return [ prefix_product[i] * suffix_product[i+1]  for i, num in enumerate(nums)]
            
            
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = suffix_product = 1
        len_nums = len(nums)
        res = []
        
        for num in nums:
            res.append(prefix_product)
            prefix_product *= num
        
        for i in range(len(nums)):
            res[len_nums - i - 1] *= suffix_product
            suffix_product *= nums[len_nums - i - 1]

        return res
            
            