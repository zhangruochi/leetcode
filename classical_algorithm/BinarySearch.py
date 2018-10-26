# 递归版本
def binarySearch(array, key, low, high):
    if high < low:
        return -1
    mid = (low + high)//2

    if array[mid] == key:
        return mid
    elif array[mid] > key:
        return binarySearch(array, key, low, mid-1)    
    else:
        return binarySearch(array,key,mid+1,high)

# 非递归版本
def binarySearch_iter(array,key):
    low,high = 0,len(array)-1

    while low <= high:
        mid = (low + high)//2
        if array[mid] < key:
            low = mid+1
        elif array[mid] > key:
            high = mid-1
        else:
            return mid        

    return -1        

if __name__ == '__main__':
    array = [1,3,4,5,6,7,8,9]
    
    print(binarySearch(array,1,0,len(array)-1))
    print(binarySearch_iter(array,1))





# 变体1，查找第一个值等于给定值的元素
def binarySearch1(nums,key,low,high):
    if high < low:
        return -1
    mid = ((high - low) >> 1) + low

    if nums[mid] < key:
        return binarySearch1(nums,key,mid+1,high )
    elif nums[mid] > key:
        return binarySearch1(nums,key,low,mid-1)
    else:
        if mid == 0 or nums[mid-1] != key: 
            return mid
        else: 
            high = mid - 1
            return binarySearch1(nums,key,low,mid-1)


# 变体2，查找最后一个值等于给定值的元素
def binarySearch2(nums,key):
    low,high,n = 0, len(nums)-1, len(nums)-1  

    while low <= high:
        mid = ((high-low) >> 1) + low

        if nums[mid] < key:
            low = mid + 1
        elif nums[mid] > key:
            high = mid - 1
        else:
            if mid == n or nums[mid+1] != key:
                return mid
            else:
                low = mid + 1 

    return -1    

# 变体3，查找第一个大于等于给定值的元素
def binarySearch3(nums,key,low,high):
    if high < low:
        return -1

    mid = ((high - low) >> 1) + low
    if nums[mid] >= key:
        if mid == 0 or nums[mid-1] < key: return mid
        else:   return binarySearch3(nums,key,low,mid-1)
    else:
        return binarySearch3(nums,key,mid+1,high)


# 变体4，查找第一个小于等于给定值的元素
def binarySearch4(nums,key):
    low,high,n = 0,len(nums)-1,len(nums)-1

    while low<= high:
        mid = ((high - low) >> 1) + low

        if nums[mid] <= key:
            if mid == n or nums[mid+1] > key: 
                return mid
            else: 
                low = mid + 1
        else:
            high = mid - 1

    return -1



# 变体5 查找第一个比某元素大的元素
def find_first_big(nums,key):
    low,high,n = 0,len(nums)-1,len(nums)-1
    while low <= high:
        mid = ((high-low)>>1) + low

        if nums[mid] <= key:
            low = mid + 1
        else:
            if mid == n or nums[mid-1] <= key:
                return nums[mid]
            else:
                high = mid - 1
    return -1    

                





if __name__ == '__main__':
    nums = [1,2,3,4,5,6,8,8,8,11,18]
    print(binarySearch1(nums,8,0,len(nums)-1))
    print(binarySearch2(nums,8))
    print(binarySearch3(nums,12,0,len(nums)-1))
    print(binarySearch4(nums,12))

    print(find_first_big(nums,8))




