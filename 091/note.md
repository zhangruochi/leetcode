## 思路


1. 满足重叠子问题，最优子结构，局部最优解无后效性

2.  状态转移方程
```Python
if s[i-1] == "0" and s[i] == "0":
    return 0
elif s[i-1] != "0" and s[i] == "0":
    if s[i-1:i+1] <= "26":
        dp.append(dp[i-2])
    else:
        return 0
elif s[i-1] == "0" and s[i] != "0":
    dp.append(dp[i-1])
else:
    if s[i-1:i+1] <= "26":
        dp.append(dp[i-2] + dp[i-1])
    else:
        dp.append(dp[i-1])
```

3. 初始状态
```Python
if s[1] == "0":
    if s[0:2] > "26":
        p = [1,0]
    else:
        dp = [1,1]
else:
    if s[0:2] > "26":
        dp = [1,1]
    else:
        dp = [1,2]
```


