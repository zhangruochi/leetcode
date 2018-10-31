>Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy algorithms are used for optimization problems

An optimization problem can be solved using Greedy if the problem has the following property: **At every step, we can make a choice that looks best at the moment, and we get the optimal solution of the complete problem.**
局部最优能导致全局最优

###  Activity Selection problem

you are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
***

The greedy choice is to always pick the next activity whose finish time is least among the remaining activities and the start time is more than or equal to the finish time of previously selected activity. We can sort the activities according to their finishing time so that we always consider the next activity as minimum finishing time activity.

1. Sort the activities according to their finishing time
2. Select the first activity from the sorted array and print it.
3. Do following for remaining activities in the sorted array.
…….a) If the start time of this activity is greater than or equal to the finish time of previously selected activity then select this activity and print it.


```Python
import random
## 活动选择问题
def get_max_activities(activities):
    activities.sort(key = lambda x:x[1])

    result = []
    for act in activities:
        if not result:
            result.append(act)

        if act[0] > result[-1][1]:
            result.append(act)

    return result

if __name__ == '__main__':
    activities = [(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)]
    random.shuffle(activities)
    print(get_max_activities(activities))
```
**How does Greedy Choice work for Activities sorted according to finish time?**
Let the given set of activities be S = {1, 2, 3, ..n} and activities be sorted by finish time. The greedy choice is to always pick activity 1. How come the activity 1 always provides one of the optimal solutions. We can prove it by showing that if there is another solution B with the first activity other than 1, then there is also a solution A of the same size with activity 1 as the first activity. Let the first activity selected by B be k, then there always exist A = {B – {k}} U {1}.(Note that the activities in B are independent and k has smallest finishing time among all. Since k is not 1, finish(k) >= finish(1)).

选择结束最早的活动总是当前的最优解，因为假设我们选择另外一个活动，总能用选择最早的活动替代这个方案



### Egyptian Fraction
Every positive fraction can be represented as sum of unique unit fractions. A fraction is unit fraction if numerator is 1 and denominator is a positive integer, for example 1/3 is a unit fraction. Such a representation is called Egyptian Fraction as it was used by ancient Egyptians.
***

We can generate Egyptian Fractions using Greedy Algorithm. For a given number of the form ‘nr/dr’ where dr > nr, first find the greatest possible unit fraction, then recur for the remaining part. 

```Python
def gcd(a,b):
    if b == 0:
        return a
    q,r = divmod(a,b)
    return gcd(b,r)

def lcm(a,b):
    return a*b//gcd(a,b)


def recursion(nr,dr,result):
    if nr == 1:
        return result + "{}/{}".format(nr,dr)

    prev = dr
    dr2 = dr//nr + 1
    dr = lcm(dr,dr2)
    nr = nr*(dr//prev) - dr//dr2

    return recursion(nr,dr,result + "{}/{} + ".format(1,dr2))




def egyptian_fraction(nr,dr):
    if dr%nr == 0:
        return "1/{}".format(dr%nr)

    return recursion(nr,dr,"")


if __name__ == '__main__':
    result = egyptian_fraction(12,13)
    print(result)
```

**How does Greedy Choice work for Egyptian Fraction subtracting greatest possible unit fraction?**

The Greedy algorithm works because a fraction is always reduced to a form where denominator is greater than numerator and numerator doesn’t divide denominator. For such reduced forms, the highlighted recursive call is made for reduced numerator. So the recursive calls keep on reducing the numerator till it reaches 1.



## 贪心算法思想：

贪心算法并不从整体最优考虑，它所作出的选择只是在某种意义上的局部最优选择。当然，希望贪心算法得到的最终结果也是整体最优的。虽然贪心算法不能对所有问题都得到整体最优解，但对许多问题它能产生整体最优解。如单源最短路经问题，最小生成树问题等。在一些情况下，即使贪心算法不能得到整体最优解，其最终结果却是最优解的很好近似。

贪心算法的基本要素：

1.贪心选择性质。所谓贪心选择性质是指所求问题的整体最优解可以通过一系列局部最优的选择，即贪心选择来达到。这是贪心算法可行的第一个基本要素，也是贪心算法与动态规划算法的主要区别。

动态规划算法通常以自底向上的方式解各子问题，而贪心算法则通常以自顶向下的方式进行，以迭代的方式作出相继的贪心选择，每作一次贪心选择就将所求问题简化为规模更小的子问题。

对于一个具体问题，要确定它是否具有贪心选择性质，必须证明每一步所作的贪心选择最终导致问题的整体最优解。

2. **当一个问题的最优解包含其子问题的最优解时**，称此问题具有最优子结构性质。问题的最优子结构性质是该问题可用动态规划算法或贪心算法求解的关键特征。

贪心算法的基本思路：

从问题的某一个初始解出发逐步逼近给定的目标，以尽可能快的地求得更好的解。当达到算法中的某一步不能再继续前进时，算法停止。

该算法存在问题：

1. 不能保证求得的最后解是最佳的；

2. 不能用来求最大或最小解问题；

3. 只能求满足某些约束条件的可行解的范围。

实现该算法的过程：

从问题的某一初始解出发；

while 能朝给定总目标前进一步 do

　　 求出可行解的一个解元素；

由所有解元素组合成问题的一个可行解；