## 思路

注意容易出现一下这种错误情况：

```
[   ["David","David0@m.co","David1@m.co"],
    ["David","David3@m.co","David4@m.co"],
    ["David","David4@m.co","David5@m.co"],
    ["David","David2@m.co","David3@m.co"],
    ["David","David1@m.co","David2@m.co"]]

-> 输出

[   ["David","David0@m.co","David1@m.co","David2@m.co"],
    ["David","David2@m.co","David3@m.co","David4@m.co","David5@m.co"] ]

-> 正确答案

[["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
```


**解决办法就是对答案进行递归调用，知道答案不再改变为止**