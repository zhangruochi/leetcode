class Solution:
    def countBits(self, num: int) -> List[int]:
        nums = [0,1,1,2]
        
        while len(nums) <= num:
            nums = nums + [1 + bit for bit in nums]
        
        return nums[:num+1]
        
        