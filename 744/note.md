## 思路

- 使用改进的二分搜索，搜索第一个比目标值大的数
- 如果不存在改值，返回第一个数
- 二分搜索的折半条件
    - 如果中值小于等于 target, 中值以及中值以前的所有数都不是我们要找的 low = mid + 1
    - 如果中值大于target,分两种情况:
        - 此时为0，说明该序列中所有数都大于 target,  返回
        - 如果 mid - 1 位置上的数小于等于target, 此即为我们要找的最小最大数，返回

```Python
class Solution(object):
    

    def binary_search(self,letters,target,n):
        low,high = 0,n
     
        while low <= high:
            mid = ((high - low) >> 1) + low
            if ord(letters[mid]) <= ord(target):
                low = mid + 1
            else:
                if mid == 0 or ord(letters[mid-1]) <= ord(target):
                    return letters[mid]
                else:
                    high = mid - 1
        return letters[0]            
                    
    
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        return self.binary_search(letters,target,len(letters)-1)
```