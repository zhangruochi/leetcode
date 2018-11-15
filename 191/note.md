## 五个函数代表不同的思考方式

```Python

    # 利用 bin 函数将 数字转化为 "ob1001.." 字符串，然后把字符串的每一位映射为相应的数字，最后把所有数字相加
    def hammingWeight(self, n):
        return reduce(add, map(int, bin(n)[2:]))

    # 直接利用字符串的 count 函数统计‘1’的数量，该方法速度非常快.    
    def hammingWeight2(self, n):
        return bin(n).count('1')

    # 利用mode 2运算，余数则为每一位的值    
    def hammingWeight3(self, n):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n //= 2
        return count

    # 000000100000 & 运算，保留原数中mask=1那一位，其它位置0
    def hammingWeight4(self, n):
        mask = 1
        count = 0
        for i in range(32):
            if n & mask != 0:
                count += 1
            mask = mask << 1

        return count

    # n&(n-1) 把 n 的最后一个不等于1的位置0    
    def hammingWeight5(self, n):
        count = 0
        while n != 0:
            n &= n - 1
            count += 1

        return count
```
![n&(n-1)](./n&(n-1).png)
