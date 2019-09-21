## 思路

1. 以 2*3 - 4*5 为例,其递归式为:

> 2*3_4*5  
> = ways(2) cartesian(*) ways(3-4*5) U  
> = ways(2*3) cartesian(-) ways(4*5) U  
> = ways(2*3-4) cartesian(*) ways(5)

2. 答案是需要所有可能的结果，比如 ways(2) = {2}, ways(3-4\*5) = {-17,-5}, 需要将ways(2) 和 ways(3-4\*5)做 cartesian product
3. 遍历字符串时，不同的分解方式做并集。



