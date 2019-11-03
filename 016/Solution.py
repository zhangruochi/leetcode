class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float("inf")
        nums.sort()
        res = None
        for i in range(len(nums)-2):
            fix = nums[i]
            left = i+1; right = len(nums)-1
            while left < right:
                tmp_sum = fix + nums[left] + nums[right]
                if abs(tmp_sum - target) < min_diff :
                    min_diff = abs(tmp_sum - target)
                    res = tmp_sum
                if tmp_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return res
                    
                    
                    
                    