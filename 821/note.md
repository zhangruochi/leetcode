## 思路

- 首先遍历一遍得到所有C所在的位置
- 分三种情况
    - 第一个C之前
    - 两个C之间（多个两两之间）
    - 最后一个C之后

```Python
def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index_c = []
        for index,char in enumerate(S):
            if char == C:
                index_c.append(index)

        result = [i for i in range(index_c[0],0,-1)]
        
        for prev,cur in zip(index_c,index_c[1:]):
            length = cur - prev
            tmp = []
            if length % 2 != 0:
                for i in range(1,length//2+1):
                    tmp.append(i)
                for i in range(length//2,0,-1):
                    tmp.append(i)
            else:
                for i in range(1,length//2+1):
                    tmp.append(i)
                for i in range(length//2-1,0,-1):
                    tmp.append(i)
            result.append(0)
            result.extend(tmp)
        result.append(0)
        for i in range(1,len(S)-index_c[-1]):
            result.append(i)
        
        return result
```