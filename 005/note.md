## 思路

- 使用中心扩散法
- 以中间某个点为中心，考虑两种情况
    - abba,abc
    - 对以上两种情况分别向左右两边扩散,同时求出最大的长度
    ```Python
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                l,h,count = i-1,i,0
                while l>=0 and h< len(s) and s[l] == s[h]:
                    count += 2
                    l-=1;h+=1
                if count > max_:
                    max_ = count
                    ans = s[l+1:h]
                    
            
            if i+1 < len(s) and s[i-1] == s[i+1]:
                l,h,count = i-1,i+1,1
                while l>=0 and h< len(s) and s[l] == s[h]:
                    count += 2
                    l-=1;h+=1
                if count > max_:
                    max_ = count
                    ans = s[l+1:h]
        ```

- 使用dp求解
- dp[i][j]:表示i到j的字符串，是不是回文串，是就为true，不是就为false。那么当s[i] == s[j]的时候，dp[i][j] = dp[i+1][j-1]
- 因此状态转移方程
**dp[i][j] = dp[i+1][j-1]**
- 遍历j,求当前j时，dp[i+1][j-1]实际上都已经求出