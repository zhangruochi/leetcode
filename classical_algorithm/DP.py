## 自顶向下备忘录
def fibonacci(n):
    memo = {}

    def fib(n,memo):
        if n in memo:
            return memo[n]
        if n <= 2:
            memo[n] = 1
        else:
            memo[n] = fib(n-1, memo) + fib(n-2,memo)
        return memo[n]

    print(fib(n,memo))

fibonacci(10)


## 自底向上备忘录
def fibonacci2(n):
    memo = [1,1]
    if n < 2:
        return memo[n]

    for i in range(2,n):
        memo.append(memo[i-1] + memo[i-2])

    print(memo[-1])    
    return memo[-1]

fibonacci2(10)




def get_max_paid():
    prev_table = {
    1:0,
    2:0,
    3:0,
    4:1,
    5:0,
    6:2,
    7:3,
    8:5
}
    price = [0,5,1,8,4,6,3,2,4]
    dp = [0]

    for i in range(1,9):
        dp.append(max(dp[i-1],dp[prev_table[i]] + price[i]))
    print(dp)
    return dp[-1]

print(get_max_paid())