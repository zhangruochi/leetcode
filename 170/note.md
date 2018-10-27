## 思路
- 该题的陷阱在于，可以 add 相同的数进去
- 用一个 table 保存加入的元素，key 为元素，value 为一个 list,保存所有值为元素的索引。
- find时，遍历 table, 分情况讨论：
    - 只有存在 tmp = value - num 时，才可能返回True
    - 存在 tmp 的情况里，如果 tmp == num, 判断 table 里是否至少两个
    - 如果 tmp != num，直接返回 True

    ```Python
    for num, indexs in self.numbers.items():
            tmp = value - num
            if tmp in self.numbers:
                if tmp == num and len(indexs) > 1:
                    return True
                if tmp != num:
                    return True
        return False
    ```
    
