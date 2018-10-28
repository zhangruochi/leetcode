##  思路
- 使用 stack 保存所有未计算 sum 的元素
- 用一个变量 depth 来保存层数
- 第一个出栈元素是list, 对 list 的每一个元素进行判断，如果是 integer, 加到 sums 中，如果是 list, 把层数添加1后一起入栈

```Python
class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
    
        nested_integer =  NestedInteger()
        for item in nestedList:
            nested_integer.add(item)
       
        sums = 0
        stack = [(nested_integer,1)]
        while stack:
            cur,depth = stack.pop()
            for item in cur.getList():
                if item.isInteger():
                    sums += depth * item.getInteger()
                else:
                    stack.append((item,depth+1))
        return sums
```