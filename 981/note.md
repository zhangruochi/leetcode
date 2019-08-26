## 思路

- 题中讲到**The timestamps for all TimeMap.set operations are strictly increasing.** 因此，我们可以用{key,[]}这样的数据结构。list 里每个元素是 (timestamps, value) 这样的 pairs. 而且，timestamps 数值上是严格递增的。
- 因为timestamps 数值上是严格递增的，可以使用二分搜索得到第一个小于等于key的timestamps.
