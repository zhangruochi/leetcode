import random
def partition(nums,left,right):
    pivot = random.randint(left,right)
    nums[pivot],nums[right] = nums[right],nums[pivot]
    
    i = left
    for j in range(left,right):
        if nums[j] < nums[right]:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
    nums[right],nums[i] = nums[i],nums[right]
    return i


def quick_sort(nums,left,right):
    if left >= right:
        return 
    pivot = partition(nums,left,right)
    quick_sort(nums,left,pivot-1)
    quick_sort(nums,pivot+1,right)

    return nums


if __name__ == '__main__':
    nums = [9,8,7,6,5,4,3,2,1]
    print(quick_sort(nums,0,len(nums)-1))