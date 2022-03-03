class Solution:
    
    def binarySearch(self,nums,target):
        start,end = 0, len(nums)-1
        
        while start <= end:
            mid = start + ((end - start) >> 1)
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[start]:
                if  target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return -1
                    
                

    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums,target)



# find pivot

def find_pivot(nums, left, right):
    if len(nums) == 1:
        return 0

    if nums[left] < nums[right]:
        return -1
    
    mid = (left + right) // 2

    if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
        return mid
    elif nums[mid] < nums[left]:
        return find_pivot(nums, left, mid)
    elif nums[mid] > nums[right]:
        return find_pivot(nums, mid, right)
    else:
        return -1


def binary_search(nums, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, target, mid+1, right)
    elif nums[mid] > target:
        return binary_search(nums, target, left, mid-1)
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        pivot = find_pivot(nums, 0, len(nums)-1)


        if pivot == -1:
            return binary_search(nums, target, 0, len(nums)-1)

        if nums[0] == target:
            return 0
        elif nums[0] > target:
            return binary_search(nums, target, pivot+1, len(nums)-1)
        elif nums[0] < target:
            return binary_search(nums, target, 0, pivot)

        

        