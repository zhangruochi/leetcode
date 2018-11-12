## 思路

- left > right 表示剩余 "(" 多于 ")",  则先用了更多的")", 情况如 "(()))",不可能匹配

```Python
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(s,left,right):
            if left > right or left < 0 or right < 0:
                return
            
            if left == 0 and right == 0:
                ans.append(s)
            
            backtrack(s+"(",left-1,right)
            backtrack(s+")",left,right-1)
            
        
        backtrack("",n,n)
        return ans
```

