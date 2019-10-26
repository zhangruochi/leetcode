# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return 
        def get_nums(root):
            if not root:
                return []
            return get_nums(root.left) + [root.val] + get_nums(root.right)
        
        def find_max(nums):
            index,max_ = 0,0
            for i,num in enumerate(nums):
                if num > max_:
                    max_ = num
                    index = i
            return index
                
        def construct(nums,root):
            if not nums: return 
            index = find_max(nums)
 
            root = TreeNode(nums[index])
            root.left = construct(nums[:index], root.left)
            root.right = construct(nums[index+1:], root.right)
            
            return root
        
        nums = get_nums(root)
        nums.append(val)
        return construct(nums,None)
        
        