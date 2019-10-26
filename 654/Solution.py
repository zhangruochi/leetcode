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
            index,max_ = 0,0
            for i,num in enumerate(nums):
                if num > max_:
                    max_ = num
                    index = i
            return index
        
        def helper(nums,root):
            if not nums:
                return 
            index = find_max(nums)
            root = TreeNode(nums[index])
            
            root.left = helper(nums[:index],root.left)
            root.right = helper(nums[index+1:],root.right)
            
            return root
        
       
        
        return helper(nums,None)