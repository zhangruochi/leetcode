# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        if not nums:
            return None
        
        def binary_search(nums,low,high):
            if low > high:
                return None
            else:
                mid = low + ((high - low) >> 1)
                root = TreeNode(nums[mid])
                root.left = binary_search(nums,low,mid-1)
                root.right = binary_search(nums,mid+1,high)
        
            return root
        
        return binary_search(nums,0,len(nums)-1)