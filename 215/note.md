## 思路

1. 和面试官沟通过的时候，明确两点

- nums这个array的大小如果很小，那么就直接Sort返回完事，没必要整那老多没用的
- 如果k的size大于len(nums)， 那么直接返回 '-1'

针对上面第一点，有了以下这个解法
```Python
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]
```

那么好，面试官说，那能轻易饶了你么，size肯定要宇宙无敌爆炸大，我就静静的看着你装逼哈。
那么我们开始考虑如何做的比nlogn更快。

### 根据Max Heap数据结构来解
> Time: O(n + klog(n)) | Space: O(n)
建堆的时间复杂度为 O(n)
```Python
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res
```

首先解释下为什么要nums = [-num for num in nums]. 因为Python的Standard Library里面调用heapify的时候，永远是一个min_heap，然后因为没有Max Heap的implementation，你要做的就是通过Min Heap来模拟Max Heap的运算，最简单的就是将所有的数变成-num，这是不是一个好的Practice？不一定，很多人也自己implement了Max Heap的数据结构。具体推荐大家看看这个帖子：StackOverFlow