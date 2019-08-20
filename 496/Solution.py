class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums1 or not nums2:
            return []
        
        dist_table = {}
        stack = []
        i = 0
        
        while i < len(nums2):
            if not stack or stack[-1] >= nums2[i]:
                stack.append(nums2[i])
                i += 1
            else:
                dist_table[stack.pop()] = nums2[i]
        
        while stack:
            dist_table[stack.pop()] = -1
        
            
        return [dist_table[num] for num in nums1]
  
                
        