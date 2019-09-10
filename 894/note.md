## 思路

1. n must be odd, If n is even, no possible trees
2. ans is the cartesian product of trees(i) and trees(n-i-1). Ans = {Tree(0, l, r) for l, r in trees(i) X trees(N – i – 1)}.

![](1.png)