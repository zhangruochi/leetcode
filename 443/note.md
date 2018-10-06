##自己的思路
1. 四个指针
    - 用一个指针 current_char 记录当前的char
    - 用一个指针 index 记录需要更新chars的位置
    - 用一个数字 count 记录当前current_char的个数
    - 用一个指针 i 遍历chars
2. 思路
    - 每当 current_char != chars[i] 时，更改current_char 为当前chars[i],count重启为0
    - 每当遇到相等的 char 时， 即 current_char == chars[i], 把相等的char全部消耗完，增加count的数量
    - 利用current_char 和 count 更新 原数组
