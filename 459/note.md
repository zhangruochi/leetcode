## 思路
- 重复数组的长度最多为原数组的一般
- 假设重复k次，则重复字符串的长度为len(s)//k
- len(s)%k == 0 必须成立
- s[0:len(s)//k] * k == s 必须成立