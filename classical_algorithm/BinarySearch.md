二分查找的对象是：有序数组。这点特别需要注意。要把数组排好序先。怎么排序，可以参看我这里多篇排序问题的文章。

基本步骤：

- 从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜素过程结束；
- 如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
- 如果在某一步骤数组为空，则代表找不到。

这种搜索算法每一次比较都使搜索范围缩小一半。时间复杂度：O(logn)

```Python
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
def binarySearch2(array,key):
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
    print(binarySearch2(array,1))
```