## 思路
- 用一个 table 记录当前 5，10，20的数量
- 每当收一个钱bill，相应 table[bill] 位置的钱数加1
- 然后判断 bill-5 能否在当前 table 中找零
- 如果队列中所有的钱都能找零，返回True
```Python
def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        table = {5:0,10:0,20:0}
        
        for bill in bills:
            table[bill] += 1
            if not self.is_changed(bill-5,table):
                return False
        return True
```

### 找零函数
- 从大往小，存在大钱就先减去大钱，然后存在小钱就减去小钱。
- 如果最后能得到0，说明找零成功。

```Python
def is_changed(self,sum_,table):
        
        if not sum_:
            return True
        
        while table[20] > 0 and sum_ - 20 >= 0:
            sum_ -= 20
            table[20] -= 1
            
        while table[10] > 0 and sum_ - 10 >= 0:
            sum_ -= 10
            table[10] -= 1
            
        while table[5] > 0 and sum_ - 5 >= 0:
            sum_ -= 5
            table[5] -= 1
        
        if sum_ == 0:
            return True
        
        return False
```