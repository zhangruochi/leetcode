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



## 活动选择问题
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




## 数字最大

def rec_opt(nums, i):
    if i == 0:
        return 1
    elif i == 1:
        return 2
    else:
        return max(nums[i]+rec_opt(nums,i-2),rec_opt(nums,i-1))

nums = [1,2,4,1,7,8,3]
print(rec_opt(nums,6))


def dp_opt(nums):
    dp = []
    dp.append(1)
    dp.append(2)
    for i in range(2,len(nums)):
        dp.append(max(nums[i]+dp[i-2],dp[i-1]))
    return dp[-1]
print(dp_opt(nums))



## 是否存在两数之和为s
nums = [3,34,4,12,5,2]

def rec_subset(nums,i,s):
    if s == 0:
        return True
    if i == 0:
        return nums[0] == s

    if nums[i] > s:
        return rec_subset(nums,i-1,s)


    return rec_subset(nums,i-1,s-nums[i]) or rec_subset(nums,i-1,s)

print(rec_subset(nums,len(nums)-1,9))
print(rec_subset(nums,len(nums)-1,46))
print(rec_subset(nums,len(nums)-1,11))



def dp_subset(nums,s):
    dp = [[]]
    



