## 思路

- 遍历 i = 1~n,
    -  如果 i 能被 3 整除且不能被5整除 ans.append("Fizz")
    -  如果 i 能被 5 整除且不能被3整除 ans.append("Buzz")
    -  如果 i 能被 3 和 5 整除 ans.append("FizzBuzz")
    -  如果非以上情况，ans.append(str(i))