class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        a = None; b = None
        count_a = 0; count_b = 0
        res = []
        
        for num in nums:
            if num == a:
                count_a +=1
            elif num == b:
                count_b += 1
            elif count_a == 0:
                count_a = 1
                a = num
            elif count_b == 0:
                count_b = 1
                b = num
            else:
                count_a -= 1
                count_b -= 1
        
        count_a_valid = 0
        count_b_valid = 0
        for num in nums:
            if num == a:
                count_a_valid += 1
            if num == b:
                count_b_valid += 1
        
        if count_a_valid > len(nums) // 3:
            res.append(a)
        if count_b_valid > len(nums) // 3:
            res.append(b)
            
        return res
        