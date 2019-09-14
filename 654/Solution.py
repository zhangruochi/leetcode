# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        if not nums:
            return 
        
        def find_max(nums):
            res = 0
            index = 0
            for i,num in enumerate(nums):
                if num > res:
                    res = num
                    index = i
            return res,index
        
        def construct(nums):
            
            if not nums:
                return None
            
            max_num,index = find_max(nums)
            root = TreeNode(max_num)
            root.left = construct(nums[0:index])
            root.right = construct(nums[index+1:])
            
            return root
        
        return construct(nums)