## 思路
- 二分搜索的变种，搜索第一个满足的答案
    ```Python
    def binarySearch(self,low, high):
            if high < low:
                return -1
            mid = low + (( high - low ) >> 1)
            if not isBadVersion(mid):
                return self.binarySearch(mid+1,high)
            else:
                if mid == 0 or not isBadVersion(mid-1):
                    return mid
                else:
                    return self.binarySearch(low,mid-1)
    ```