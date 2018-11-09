## 思路

- 求X 的 N 次方，只要求两个 N/2 次方再相乘
- 递归求解时，使用 memo 记录已经求过的答案
        ```Python
        def rec_pow(x,n,memo):
            if n in memo:
                return memo[n]
            
            if n == 0:
                return 1
            if n == 1:
                return x
        
            memo[n] = rec_pow(x,n//2,memo) * rec_pow(x,n-n//2,memo)
            return memo[n]
        ```
- 上述答案中，如果不适用memo, 每个rec_pow都要求解两次，因为递归没有记忆能力