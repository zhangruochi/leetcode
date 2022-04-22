LeetCode solutions in Python3.
========


Table of Contents
=================

   * [LeetCode](#leetcode)
      * [Complexity](#complexity)
      * [Classical Algorithm](#classical-data-structure-and-algorithm)
      * [Bit Manipulation](#bit-manipulation)
      * [Array](#array)
      * [Linked List](#linked-List)
      * [Stack](#stack)
      * [Recursion](#recursion)
      * [Queue](#queue)
      * [Binary Tree](#binary-tree)
      * [Divide and Conquer](#divide-and-conquer)
      * [Hash Table](#hash-table)
      * [Sort](#sort)
      * [Heap](#heap)
      * [Math](#math)
      * [Binary Search](#binary-search)
      * [Binary Search Tree](#binary-search-tree)
      * [N-ary Tree](#n-ary-tree)
      * [Graph](#graph)
      * [BackTracking](#backtracking)
      * [BFS](#bfs)
      * [DFS](#dfs)
      * [Greedy](#greedy)
      * [Design](#design)
      * [Dynamic Programming](#dynamic-programming)
      * [SQL Schema](#sql-schema)
      * [剑指offer](#剑指offer)
      * [程序员面试经典](#程序员面试经典)

      

## Complexity
[Time & Space Complexity](./classical_algorithm/TimeSpaceCpmlexity.md)

## Data Structure
| Name. | Note |
| --- | ----- |
| [BST](./classical_algorithm/BinarySearchTree.py) | [NOTE](./classical_algorithm/BST.md)
| Graph| [NOTE](./classical_algorithm/Graph.md)
| [Trie](./classical_algorithm/Trie.py)|[NOTE](./classical_algorithm/Trie.md)
| [Union Find](./classical_algorithm/UnionFind.py)|[NOTE](./classical_algorithm/UnionFind.md)
| [Queue](./classical_algorithm/queue.py) | [NOTE](./classical_algorithm/queue.md)


## Classical Algorithm
| Name. | Note |
| --- | ----- |
| [KMP](./classical_algorithm/kmp.py) | [NOTE](./classical_algorithm/kmp.md)
| Recursion | [NOTE](./classical_algorithm/Recursion.md)
| [Dijkstra](./classical_algorithm/Dijkstra.py) | [NOTE](./classical_algorithm/Dijkstra.md)
| Floyd |[NOTE](./classical_algorithm/Floyd.md)
| [BinarySearch](./classical_algorithm/BinarySearch.py)|[NOTE](./classical_algorithm/BinarySearch.md)
| [Sort](./classical_algorithm/Sort.py)|[NOTE](./classical_algorithm/Sort.md)
| [Heap and HeapSort](./classical_algorithm/MyHeap.py)| NOTE
| [Greedy](./classical_algorithm/Greedy.py)|[NOTE](./classical_algorithm/Greedy.md)
| [Dynamic Programming](./classical_algorithm/DP.py)|[NOTE](./classical_algorithm/DP.md)
| [Eight Queue](./classical_algorithm/eight_queue.py)|Backtracking
| [Hamilton circuit](./classical_algorithm/hamilton.py)|Backtracking
| BFS(unweighted graph shortest path) |[NOTE](./classical_algorithm/BFS.md)
| [Tree Traverse](./classical_algorithm/TreeTraverse.py) | [NOTE](./classical_algorithm/TreeTraverse.md)
| [Knapsack](./classical_algorithm/Knapsack.py) | 


## Bit Manipulation
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.136|[Single Number](https://leetcode.com/problems/single-number/)|[Solution](./136/Solution.py)|[Note](./136/note.md)|Easy|O(n)|O(1)||
|No.191|[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)|[Solution](./191/Solution.py)|[Note](./191/note.md)|Easy|O(1)|O(1)||
|No.190|[Reverse Bits](https://leetcode.com/problems/reverse-bits/)|[Solution](./190/Solution.py)|[Note](./190/note.md)|Easy|O(1)|O(1)||
|No.231|[Power of Two](https://leetcode.com/problems/power-of-two/)|[Solution](./231/Solution.py)|[Note](./231/note.md)|Easy|O(1)|O(1)||
|No.342|[Power of Four](https://leetcode.com/problems/power-of-four/submissions/)|[Solution](./342/Solution.py)|[Note](./342/note.md)|Easy|O(1)|O(1)||
|No.401|[Binary Watch](https://leetcode.com/problems/binary-watch/)|[Solution](./401/Solution.py)|[Note](./401/note.md)|Easy|O(1)|O(1)||
|No.461|[Hamming Distance](https://leetcode.com/problems/hamming-distance/)|[Solution](./461/Solution.py)|[Note](./461/note.md)|Easy|O(1)|O(1)||
|No.645|[Set Mismatch](https://leetcode.com/problems/set-mismatch/)|[Solution](./645/Solution.py)|[Note](./645/note.md)|Easy|O(n)|O(1)||
|No.137|[Single NumberII](https://leetcode.com/problems/single-number-ii/)|[Solution](./137/Solution.py)|[Note](./137/note.md)|Medium|O(n)|O(1)||
|No.762|[Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)|[Solution](./762/Solution.py)|[Note](./762/note.md)|Medium|O(1)|O(1)||
|No.371|[Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)|[Solution](./371/Solution.py)|[Note](./371/note.md)|Easy|O(1)|O(1)||
|No.268|[Missing Number](https://leetcode.com/problems/missing-number/)|[Solution](./268/Solution.py)|[Note](./268/note.md)|Easy|O(n)|O(1)|,Math|
|No.1085|[Sum of Digits in the Minimum Number](https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/)|[Solution](./1085/Solution.py)|[Note](./1085/note.md)|Easy|O(n)|O(1)||
|No.728|[Self Dividing Numbers](https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/)|[Solution](./728/Solution.py)|[Note](./728/note.md)|Easy|O(nm)|O(1)||
|No.319|[Bulb Switcher](https://leetcode.com/problems/bulb-switcher/)|[Solution](./319/Solution.py)|[Note](./319/note.md)|Medium|O(n)|O(1)||
|No.201|[Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)|[Solution](./201/Solution.py)|[Note](./201/note.md)|Medium|O(1)|O(1)||


## Two Pointer
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.011|[Container With Most Water](https://leetcode.com/problems/container-with-most-water/submissions/)|[Solution](./011/Solution.py)|[Note](./011/note.md)|Medium|O(n)|O(1)|two pointer|
|No.209|[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)|[Solution](./209/Solution.py)|[Note](./209/note.md)|Medium|O(n)|O(1)|two pointer|
|No.083|[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)|[Solution](./083/Solution.py)|[Note](./083/note.md)|Easy|O(n)|O(1)|two pointer|
|No.922|[Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)|[Solution](./922/Solution.py)|[Note](./922/note.md)|Easy|O(n)|O(1)|two pointer|
|No.904|[Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)|[Solution](./904/Solution.py)|[Note](./904/note.md)|Medium|O(n)|O(1)|two pointer|
|No.986|[Interval List Intersections](https://leetcode-cn.com/problems/interval-list-intersections/)|[Solution](./986/Solution.py)|[Note](./986/note.md)|Medium|O(n)|O(1)|two pointer|
|No.1099|[Two Sum Less Than K](https://leetcode-cn.com/problems/two-sum-less-than-k/)|[Solution](./1099/Solution.py)|[Note](./1099/note.md)|Easy|O(n)|O(1)|two pointer|


## Array
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.026|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|[Python](./026/Solution.py) [C++](./026/Solution.cpp)|[Note](./026/note.md)|Easy|O(n)|O(1)|Array|
|No.027|[Remove Element](https://leetcode.com/problems/remove-element/)|[Solution](./027/Solution.py)|[Note](./027/note.md)|Easy|O(n)|O(1)||
|No.066|[Plus One](https://leetcode.com/problems/plus-one/)|[Solution](./066/Solution.py)|[Note](./066/note.md)|Easy|O(n)|O(1)||
|No.118|[Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)|[Solution](./118/Solution.py)|[Note](./118/note.md)|Easy|O(n^2)|O(1)||
|No.119|[Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)|[Solution](./119/Solution.py)|[Note](./119/note.md)|Easy|O(n^2)|O(1)||
|No.121|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|[Solution](./121/Solution.py)|[Note](./121/note.md)|Easy|O(n)|O(1)|Array|
|No.169|[Majority Element](https://leetcode.com/problems/majority-element/)|[Solution](./169/Solution.py)|[Note](./169/note.md)|Easy|O(n)|O(1)||
|No.189|[Rotate Array](https://leetcode.com/problems/rotate-array/)|[Solution](./189/Solution.py)|[Note](./189/note.md)|Easy|O(n)|O(1)||
|No.905|[Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)|[Solution](./905/Solution.py)|[Note](./905/note.md)|Easy|O(n)|O(1)||
|No.896|[Monotonic Array](https://leetcode.com/problems/monotonic-array/)|[Solution](./896/Solution.py)|[Note](./896/note.md)|Easy|O(n)|O(1)||
|No.243|[Shortest Word Distance](https://leetcode.com/problems/shortest-word-distance/)|[Solution](./243/Solution.py)|[Note](./243/note.md)|Easy|O(n)|O(1)||
|No.448|[Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)|[Solution](./448/Solution.py)|[Note](./448/note.md)|Easy|O(n)|O(1)||
|No.821|[Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/)|[Solution](./821/Solution.py)|[Note](./821/note.md)|Easy|O(n)|O(n)||
|No.001|[Two Sum](https://leetcode.com/problems/two-sum/)|[Solution](./001/Solution.py)|[Note](./001/note.md)|Easy|O(n)|O(n)||
|No.167|[Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)|[Solution](./167/Solution.py)|[Note](./167/note.md)|Easy|O(n)|O(1)||
|No.170|[Two Sum III](https://leetcode.com/problems/two-sum-iii-data-structure-design/)|[Solution](./170/Solution.py)|[Note](./170/note.md)|Easy|O(n)|O(1)||
|No.867|[Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)|[Solution](./868/Solution.py)|[Note](./868/note.md)|Easy|O(n)|O(n)||
|No.860|[Lemonade Change](https://leetcode.com/problems/lemonade-change/)|[Solution](./860/Solution.py)|[Note](./860/note.md)|Easy|O(n)|O(n)||
|No.849|[Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/)|[Solution](./849/Solution.py)|[Note](./849/note.md)|Easy|O(n)|O(1)||
|No.840|[Magic Squares In Grid](https://leetcode.com/problems/magic-squares-in-grid/)|[Solution](./840/Solution.py)|[Note](./840/note.md)|Easy|O(n)|O(1)||
|No.283|[Move Zeroes](https://leetcode.com/problems/move-zeroes/)|[Solution](./283/Solution.py)|[Note](./283/note.md)|Easy|O(n)|O(1)||
|No.015|[3sum](https://leetcode.com/problems/3sum/)|[Solution](./015/Solution.py)|[Note](./015/note.md)|Easy|O(n^2)|O(n)||
|No.560|[Subarray Sum Equals k](https://leetcode.com/problems/subarray-sum-equals-k/)|[Solution](./560/Solution.py)|[Note](./560/note.md)|Medium|O(n)|O(1)|prefix sum|
|No.325|[Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)|[Solution](./325/Solution.py)|[Note](./325/note.md)|Medium|O(n)|O(n)|prefix sum|
|No.930|[Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/)|[Solution](./930/Solution.py)|[Note](./930/note.md)|Medium|O(n)|O(n)|prefix sum|
|No.674|[Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)|[Solution](./674/Solution.py)|[Note](./674/note.md)|Easy|O(n)|O(1)||
|No.031|[Next Permutation](https://leetcode.com/problems/next-permutation/)|[Solution](./031/Solution.py)|[Note](./031/note.md)|Medium|O(nlogn)|O(1)||
|No.422|[Valid Word Square](https://leetcode.com/problems/valid-word-square/)|[Solution](./422/Solution.py)|[Note](./422/note.md)|Easy|O(n^2)|O(1)||
|No.349|[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/submissions/)|[Solution](./349/Solution.py)|[Note](./349/note.md)|Easy|O(n)|O(1)||
|No.724|[Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)|[Solution](./724/Solution.py)|[Note](./724/note.md)|Easy|O(n)|O(1)||
|No.747|[Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/)|[Solution](./747/Solution.py)|[Note](./747/note.md)|Easy|O(n)|O(1)||
|No.498|[Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/)|[Solution](./498/Solution.py)|[Note](./498/note.md)|Medium|O(n)|O(n)||
|No.561|[Array Partition I](https://leetcode.com/problems/array-partition-i/)|[Solution](./561/Solution.py)|[Note](./561/note.md)|Easy|O(nlogn)|O(1)||
|No.485|[Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)|[Solution](./485/Solution.py)|[Note](./485/note.md)|Easy|O(n)|O(1)||
|No.1086|[High Five](https://leetcode.com/problems/high-five/)|[Solution](./1086/Solution.py)|[Note](./1086/note.md)|Easy|O(n^2logn)|O(n)||
|No.1064|[Fixed Point](https://leetcode.com/problems/fixed-point/)|[Solution](./1064/Solution.py)|[Note](./1064/note.md)|Easy|O(n)|O(n)||
|No.832|[Flipping an Image](https://leetcode.com/problems/flipping-an-image/)|[Solution](./832/Solution.py)|[Note](./832/note.md)|Easy|O(n)|O(n)||
|No.053|[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|[Solution](./053/Solution.py)|[Note](./053/note.md)|Easy|O(n)|O(n)|cum sum|
|No.240|[Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)|[Solution](./240/Solution.py)|[Note](./240/note.md)|Easy|O(N+M)|O(1)||
|No.961|[N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)|[Solution](./961/Solution.py)|[Note](./961/note.md)|Easy|O(n)|O(n)||
|No.977|[Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)|[Solution](./977/Solution.py)|[Note](./977/note.md)|Easy|O(n)|O(n)||
|No.016|[3Sum Closest](https://leetcode.com/problems/3sum-closest/)|[Solution](./016/Solution.py)|[Note](./016/note.md)|Medium|O(n^2)|O(1)||
|No.1207|[Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/)|[Solution](./1207/Solution.py)|[Note](./1207/note.md)|Easy|O(n)|O(n)||
|No.338|[Counting Bits](https://leetcode.com/problems/counting-bits/)|[Solution](./338/Solution.py)|[Note](./338/note.md)|Medium|O(n)|O(n)||
|No.259|[3sum Smaller](https://leetcode.com/problems/counting-bits/)|[Solution](./259/Solution.py)|[Note](./259/note.md)|Medium|O(n^2)|O(1)||
|No.1007|[Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)|[Solution](./1007/Solution.py)|[Note](./1007/note.md)|Medium|O(n)|O(1)||
|No.041|[First Missing Positive](https://leetcode.com/problems/first-missing-positive/)|[Solution](./041/Solution.py)|[Note](./041/note.md)|Hard|O(n)|O(1)||
|No.229|[Majority Element II](https://leetcode.com/problems/majority-element-ii/)|[Solution](./229/Solution.py)|[Note](./229/note.md)|Hard|O(n)|O(n)||
|No.923|[3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/)|[Solution](./923/Solution.py)|[Note](./923/note.md)|Meidum|O(n^2)|O(n)||
|No.891|[Sum of Subsequence Widths](https://leetcode.com/problems/sum-of-subsequence-widths/)|[Solution](./891/Solution.py)|[Note](./891/note.md)|Hard|O(n^2)|O(n)||
|No.900|[RLE Iterator](https://leetcode.com/problems/rle-iterator/)|[Solution](./900/Solution.py)|[Note](./900/note.md)|Medium|O(n)|O(n)||
|No.228|[Summary Ranges](https://leetcode.com/problems/summary-ranges/)|[Solution](./228/Solution.py)|[Note](./228/note.md)|Medium|O(n)|O(n)||
|No.665|[Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/)|[Solution](./665/Solution.py)|[Note](./665/note.md)|Easy|O(n)|O(1)||
|No.463|[Island Perimeter](https://leetcode.com/problems/island-perimeter/)|[Solution](./463/Solution.py)|[Note](./463/note.md)|Easy|O(n)|O(1)||
|No.948|[Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/)|[Solution](./948/Solution.py)|[Note](./948/note.md)|Medium|O(n)|O(1)||
|No.667|[Beautiful Arrangement II](https://leetcode.com/problems/beautiful-arrangement-ii/)|[Solution](./667/Solution.py)|[Note](./667/note.md)|Medium|O(n)|O(n)||
|No.419|[Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/)|[Solution](./419/Solution.py)|[Note](./419/note.md)|Medium|O(nm)|O(1)||
|No.1014|[Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair/)|[Solution](./1014/Solution.py)|[Note](./1014/note.md)|Medium|O(n)|O(1)||
|No.122|[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)|[Solution](./122/Solution.py)|[Note](./122/note.md)|Easy|O(n)|O(1)||
|No.080|[Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)|[Solution](./080/Solution.py)|[Note](./080/note.md)|Medium|O(n)|O(1)||
|No.525|[Contiguous Array](https://leetcode.com/problems/contiguous-array/)|[Solution](./525/Solution.py)|[Note](./525/note.md)|Medium|O(n)|O(n)||
|No.054|[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)|[Note](./054/note.md)|Medium|O(n)|O(n)||
|No.547|[Number of Provinces](https://leetcode-cn.com/problems/number-of-provinces/)|[Note](./547/note.md)|Medium|O(n^2)|O()|Union Found|
|No.566|[Reshape the Matrix](https://leetcode-cn.com/problems/reshape-the-matrix/)|[Note](./566/note.md)|Medium|O(n^2)|O()||
|No.073|[Set Matrix Zeroes](https://leetcode-cn.com/problems/set-matrix-zeroes/)|[Note](./073/note.md)|Medium|O(nm)|O()||
|No.128|[Longest Consecutive Sequence](https://leetcode-cn.com/problems/longest-consecutive-sequence/)|[Note](./128/note.md)|Medium|O(n)|O(n)||
|No.043|[Multiply Strings](https://leetcode-cn.com/problems/multiply-strings/)|[Note](./043/note.md)|Medium|O(nm)|O(n)||
|No.048|[Rotate Image](https://leetcode-cn.com/problems/rotate-image/)|[Note](./048/note.md)|Medium|O(nm)|O(nm)||



## String
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.014|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)|[Solution](./014/Solution.py)|[Note](./014/note.md)|Easy|O(n)|O(1)|String|
|No.028|[Implement strStr()](https://leetcode.com/problems/implement-strstr/)|[Solution](./028/Solution.py)|[Note](./028/note.md)|Easy|O(n + k)|O(1)|kmp|
|No.038|[Count and Say](https://leetcode.com/problems/count-and-say/)|[Solution](./038/Solution.py)|[Note](./038/note.md)|Easy|O(n * 2)|O(1)|iteration|
|No.058|[Length of Last Word](https://leetcode.com/problems/length-of-last-word/)|[Solution](./058/Solution.py)|[Note](./058/note.md)|Easy|O(n)|O(1)|count from back|
|No.067|[Add Binary](https://leetcode.com/problems/add-binary/)|[Solution](./067/Solution.py)|[Note](./067/note.md)|Easy|O(n)|O(1)|construction number|
|No.125|[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)|[Solution](./125/Solution.py)|[Note](./125/note.md)|Easy|O(n)|O(n)||
|No.165|[Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/)|[Solution](./165/Solution.py)|[Note](./165/note.md)|Easy|O(n)|O(n)||
|No.434|[Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/)|[Solution](./434/Solution.py)|[Note](./434/note.md)|Easy|O(n)|O(1)||
|No.443|[String Compression](https://leetcode.com/problems/string-compression/)|[Solution](./443/Solution.py)|[Note](./443/note.md)|Easy|O(n)|O(1)|many pointer|
|No.459|[Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)|[Solution](./459/Solution.py)|[Note](./459/note.md)|Easy|O(n)|O(1)|kmp|
|No.006|[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)|[Solution](./006/Solution.py)|[Note](./006/note.md)|Meduim|O(n * k)|O(1)|String|
|No.521|[Longest Uncommon Subsequence I](https://leetcode.com/problems/longest-uncommon-subsequence-i/)|[Solution](./521/Solution.py)|[Note](./521/note.md)|Easy|O(n * k)|O(1)|String|
|No.680|[Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/submissions/)|[Solution](./680/Solution.py)|[Note](./680/note.md)|Easy|O(n)|O(1)|String|
|No.681|[Next Closest Time](https://leetcode.com/problemset/all/)|[Solution](./681/Solution.py)|[Note](./681/note.md)|Medium|O(4^4)|O(1)|DFS|
|No.771|[Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)|[Solution](./771/Solution.py)|[Note](./771/note.md)|Easy|O(n)|O(n)||
|No.482|[License Key Formatting](https://leetcode.com/problems/license-key-formatting/)|[Solution](./482/Solution.py)|[Note](./482/note.md)|Easy|O(n)|O(n)||
|No.344|[Reverse String](https://leetcode.com/problems/reverse-string/)|[Solution](./344/Solution.py)|[Note](./344/note.md)|Easy|O(n)|O(1)||
|No.412|[Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)|[Solution](./412/Solution.py)|[Note](./412/note.md)|Easy|O(n)|O(1)||
|No.005|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)|[Solution](./005/Solution.py)|[Note](./005/note.md)|Medium|O(n^2)|O(1)||
|No.819|[Most Common Word](https://leetcode.com/problems/most-common-word/)|[Solution](./819/Solution.py)|[Note](./819/note.md)|Easy|O(n)|O(n)||
|No.929|[Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/)|[Solution](./929/Solution.py)|[Note](./929/note.md)|Easy|O(n^2)|O(n)||
|No.535|[Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/)|[Solution](./535/Solution.py)|[Note](./535/note.md)|Meduim|O(n)|O(n)||
|No.271|[Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)|[Solution](./271/Solution.py)|[Note](./271/note.md)|Meduim|O(n)|O(n)||
|No.003|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)|[Solution](./003/Solution.py)|[Note](./003/note.md)|Meduim|O(n)|O(n)||
|No.293|[Flip Game](https://leetcode.com/problems/flip-game/)|[Solution](./293/Solution.py)|[Note](./293/note.md)|Easy|O(n)|O(n)||
|No.604|[Design Compressed String Iterator](https://leetcode.com/problems/design-compressed-string-iterator/)|[Solution](./293/Solution.py)|[Note](./293/note.md)|Easy|O(n)|O(n)|Iterator|
|No.008| [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)|[Solution](./008/Solution.py)|[Note](./008/note.md)|Meduim|O(n)|O(n)||
|No.151| [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)|[Solution](./151/Solution.py)|[Note](./151/note.md)|Meduim|O(n)|O(n)||
|No.557| [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)|[Solution](./557/Solution.py)|[Note](./557/note.md)|Easy|O(n)|O(1)||
|No.1108| [Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/)|[Solution](./1108/Solution.py)|[Note](./1108/note.md)|Easy|O(n)|O(1)||
|No.1180| [Count Substrings with Only One Distinct Letter](https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/)|[Solution](./1180/Solution.py)|[Note](./1180/note.md)|Easy|O(n)|O(1)||
|No.1134| [Armstrong Number](https://leetcode.com/problems/armstrong-number/)|[Solution](./1134/Solution.py)|[Note](./1134/note.md)|Easy|O(n)|O(1)||
|No.709| [To Lower Case](https://leetcode.com/problems/to-lower-case/)|[Solution](./709/Solution.py)|[Note](./709/note.md)|Easy|O(n)|O(1)||
|No.657| [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/)|[Solution](./657/Solution.py)|[Note](./657/note.md)|Easy|O(n)|O(n)||
|No.1221| [Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/)|[Solution](./1221/Solution.py)|[Note](./1221/note.md)|Easy|O(n)|O(1)||
|No.214| [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)|[Solution](./214/Solution.py)|[Note](./214/note.md)|Hard|O(n^2)|O(n)||
|No.838| [Push Dominoes](https://leetcode.com/problems/push-dominoes/)|[Solution](./838/Solution.py)|[Note](./838/note.md)|Medium|O(n)|O(n)||
|No.409| [Push Dominoes](https://leetcode.com/problems/longest-palindrome/)|[Solution](./409/Solution.py)|[Note](./409/note.md)|Easy|O(n)|O(n)||
|No.520| [Detect Capital](https://leetcode.com/problems/detect-capital/)|[Solution](./520/Solution.py)|[Note](./520/note.md)|Easy|O(1)|O(1)||
|No.791| [Custom Sort String](https://leetcode.com/problems/custom-sort-string/)|[Solution](./791/Solution.py)|[Note](./791/note.md)|Medium|O(n)|O(n)||
|No.1163| [Last Substring in Lexicographical Order](https://leetcode.com/problems/last-substring-in-lexicographical-order/)|[Solution](./1163/Solution.py)|[Note](./1163/note.md)|Hard|O(n^2)|O(1)||
|No.1790| [Check if One String Swap Can Make Strings Equal](https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal/)|[Solution](./1790/Solution.py)|[Note](./1790/note.md)|Easy|O(n)|O(1)||
|No.438| [Find All Anagrams in a String](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)|[Solution](./438/Solution.py)|[Note](./438/note.md)|Medium|O(n)|O(n)||
|No.383| [Ransom Note](https://leetcode-cn.com/problems/ransom-note/)|[Solution](./383/Solution.py)|[Note](./383/note.md)|Medium|O(n)|O(n)||
|No.012| [Integer to Roman](https://leetcode-cn.com/problems/integer-to-roman/)|[Solution](./012/Solution.py)|[Note](./012/note.md)|Medium|O(n)|O(n)||
|No.013| [Roman to Integer](https://leetcode-cn.com/problems/roman-to-integer/)|[Solution](./013/Solution.py)|[Note](./013/note.md)|Easy|O(n)|O(n)||
|No.294| [Flip Game II](https://leetcode-cn.com/problems/flip-game-ii/)|[Solution](./294/Solution.py)|[Note](./294/note.md)|Medium|O(n^n)|O(n)||

## Linked List
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.021|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|[Solution](./021/Solution.py)|[Note](./021/note.md)|Easy|O(n)|O(1)|guard node|
|No.024|[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) |[Solution](./024/Solution.py)|[Note](./024/note.md)|Medium|O(n)|O(1)|watch end|
|No.160|[Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)|[Solution](./160/Solution.py)|[Note](./160/note.md)|Easy|O(n)|O(1)||
|No.203|[Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)|[Solution](./203/Solution.py)|[Note](./203/note.md)|Easy|O(n)|O(1)||
|No.237|[Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)|[Solution](./237/Solution.py)|[Note](./237/note.md)|Easy|O(1)|O(1)|tricky,del|
|No.234|[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)|[Solution](./234/Solution.py)|[Note](./234/note.md)|Meduim|O(1)|O(1)|slow,quick pointer|
|No.206|[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)|[Solution](./206/Solution.py)|[Note](./206/note.md)|Easy|O(n)|O(1)|reverse|
|No.002|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|[Solution](./002/Solution.py)|[Note](./002/note.md)|Medium|O(n)|O(1)||
|No.019|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|[Solution](./019/Solution.py)|[Note](./019/note.md)|Medium|O(n)|O(1)|quick slow pointer|
|No.141|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)|[Solution](./141/Solution.py)|[Note](./141/note.md)|Easy|O(n)|O(1)|quick slow pointer|
|No.142|[Linked List CycleII](https://leetcode.com/problems/linked-list-cycle-ii/)|[Solution](./142/Solution.py)|[Note](./142/note.md)|Medium|O(n)|O(1)|quick slow pointer|
|No.023|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)|[Solution](./023/Solution.py)|[Note](./023/note.md)|Hard|O(nlogn)|O(nk)||
|No.138|[Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)|[Solution](./138/Solution.py)|[Note](./138/note.md)|Medium|O(n)|O(n)||
|No.061|[Rotate List](https://leetcode.com/problems/rotate-list/)|[Solution](./061/Solution.py)|[Note](./061/note.md)|Medium|O(n)|O(n)||
|No.082|[Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)|[Note](./082/note.md)|[Solution](./061/Solution.py)|Medium|O(n)|O(n)||
|No.086|[Partition List](https://leetcode.com/problems/partition-list/)|[Note](./086/note.md)|[Solution](./061/Solution.py)|Medium|O(n)|O(n)||
|No.092|[Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)|[Note](./092/note.md)|[Solution](./061/Solution.py)|Medium|O(n)|O(n)||
|No.143|[Reorder List](https://leetcode.com/problems/reorder-list/)|[Note](./143/note.md)|Medium|[Solution](./061/Solution.py)|O(n)|O(n)||
|No.876|[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)|[Note](./876/note.md)|[Solution](./876/Solution.py)|Easy|O(n)|O(1)||
|No.061|[Rotate List](https://leetcode-cn.com/problems/rotate-list/)|[Note](./061/note.md)|[Solution](./061/Solution.py)|Meduim|O(n)|O(1)||






## Stack
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.020|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|[Solution](./020/Solution.py)|[Note](./020/note.md)|Easy|O(n)|O(1)||
|No.844|[Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)|[Solution](./844/Solution.py)|[Note](./844/note.md)|Easy|O(M+N)|O(1)||
|No.155|[Min Stack](https://leetcode.com/problems/min-stack/)|[Solution](./155/Solution.py)|[Note](./155/note.md)|Easy|O(1)|O(1)||
|No.173|[Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)|[Solution](./173/Solution.py)|[Note](./173/note.md)|Medium|O(n)|O(1)||
|No.232|[Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)|[Solution](./232/Solution.py)|[Note](./232/note.md)|Easy|O(n)|O(1)||
|No.682|[Baseball Game](https://leetcode.com/problems/baseball-game/)|[Solution](./682/Solution.py)|[Note](./682/note.md)|Easy|O(n)|O(1)||
|No.056|[Merge Intervals](https://leetcode.com/problems/merge-intervals/)|[Solution](./056/Solution.py)|[Note](./056/note.md)|Medium|O(nlogn)|O(n)||
|No.057|[Insert Interval](https://leetcode.com/problems/insert-interval/)|[Solution](./057/Solution.py)|[Note](./057/note.md)|Hard|O(n)|O(n)||
|No.394|[Decode String](https://leetcode.com/problems/decode-string/)|[Solution](./394/Solution.py)|[Note](./394/note.md)|Medium|O(n)|O(n)||
|No.921|[Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)|[Solution](./921/Solution.py)|[Note](./921/note.md)|Medium|O(n)|O(n)||
|No.339|[Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/)|[Solution](./339/Solution.py)|[Note](./339/note.md)|Easy|O(n)|O(1)|DFS|
|No.716|[Max Stack](https://leetcode.com/problems/max-stack/)|[Solution](./716/Solution.py)|[Note](./716/note.md)|Easy|O(n)|O(1)|DFS|
|No.946|[Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/)|[Solution](./946/Solution.py)|[Note](./946/note.md)|Medium|O(n)|O(n)||
|No.071|[Simplify Path](https://leetcode.com/problems/simplify-path/)|[Solution](./071/Solution.py)|[Note](./071/note.md)|Medium|O(n)|O(n)||
|No.150|[Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)|[Solution](./150/Solution.py)|[Note](./150/note.md)|Medium|O(n)|O(n)||
|No.225|[Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)|[Solution](./225/Solution.py)|[Note](./225/note.md)|Easy|O(n)|O(n)||
|No.341|[Flatten Nested List Iterator](https://leetcode.com/problems/implement-stack-using-queues/)|[Solution](./341/Solution.py)|[Note](./341/note.md)|Easy|O(n)|O(n)||
|No.439|[Ternary Expression Parser](https://leetcode.com/problems/ternary-expression-parser/)|[Solution](./439/Solution.py)|[Note](./439/note.md)|Medium|O(n)|O(n)||
|No.042|[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)|[Solution](./042/Solution.py)|[Note](./042/note.md)|Hard|O(n)|O(n)||
|No.084|[Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)|[Solution](./084/Solution.py)|[Note](./084/note.md)|Hard|O(n)|O(n)||
|No.496|[Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)|[Solution](./496/Solution.py)|[Note](./496/note.md)|Easy|O(n)|O(n)||
|No.1021|[Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)|[Solution](./1021/Solution.py)|[Note](./1021/note.md)|Easy|O(n)|O(n)||
|No.1081|[Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)|[Solution](./1081/Solution.py)|[Note](./1081/note.md)|Medium|O(n)|O(n)||
|No.735|[Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)|[Solution](./735/Solution.py)|[Note](./735/note.md)|Medium|O(n)|O(n)||
|No.328|[Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)|[Solution](./328/Solution.py)|[Note](./328/note.md)|Medium|O(n)|O(n)||
|No.678|[Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)|[Solution](./678/Solution.py)|[Note](./678/note.md)|Medium|O(n)|O(n)||
|No.offer09|[剑指 Offer 09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)|[Solution](./offer09/Solution.py)|[Note](./offer09/note.md)|Easy|O(n)|O(n)||
|No.739|[Daily Temperatures](https://leetcode-cn.com/problems/daily-temperatures/)|[Solution](./739/Solution.py)|[Note](./739/note.md)|Medium|O(n)|O(n)||



## Recursion
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.101|[Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)|[Solution](./101/Solution.py)|[Note](./101/note.md)|Easy|O(n)|O(h)||
|No.872|[Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)|[Solution](./872/Solution.py)|[Note](./872/note.md)|Easy|O(n)|O(n)||
|No.104|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[Solution](./104/Solution.py)|[Note](./104/note.md)|Easy|O(logn)|O(1)||
|No.110|[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)|[Solution](./110/Solution.py)|[Note](./110/note.md)|Easy|O(logn)|O(1)||
|No.111|[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[Solution](./111/Solution.py)|[Note](./111/note.md)|Easy|O(logn)|O(1)||
|No.404|[Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)|[Solution](./404/Solution.py)|[Note](./404/note.md)|Easy|O(logn)|O(1)||
|No.669|[Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)|[Solution](./669/Solution.py)|[Note](./669/note.md)|Easy|O(logn)|O(1)||
|No.671|[Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/)|[Solution](./671/Solution.py)|[Note](./671/note.md)|Easy|O(logn)|O(1)||
|No.894|[All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/)|[Solution](./894/Solution.py)|[Note](./894/note.md)|Easy|O(2^N)|O(n)||
|No.1137|[N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)|[Solution](./1137/Solution.py)|[Note](./1137/note.md)|Easy|O(n)|O(n)||
|No.544|[Output Contest Matches](https://leetcode.com/problems/output-contest-matches/)|[Solution](./544/Solution.py)|[Note](./544/note.md)|Medium|O(n)|O(n)||
|No.247|[Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/)|[Solution](./247/Solution.py)|[Note](./247/note.md)|Medium|O(n)|O(n)||
|No.721|[Accounts Merge](https://leetcode.com/problems/accounts-merge/)|[Solution](./721/Solution.py)|[Note](./721/note.md)|Medium|O(n^2)|O(n)||
|No.988|[Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/)|[Solution](./988/Solution.py)|[Note](./988/note.md)|Medium|O(n)|O(n)||



## Queue
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.346|[Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)|[Solution](./346/Solution.py)|[Note](./346/note.md)|Easy|O(1)|O(w)||
|No.281|[Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/)|[Solution](./281/Solution.py)|[Note](./281/note.md)|Medium|O(n)|O(n)||
|No.127|[Word Ladder](https://leetcode.com/problems/word-ladder/)|[Solution](./127/Solution.py)|[Note](./127/note.md)|Medium|O(n)|O(n)||
|No.622|[Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)|[Solution](./622/Solution.py)|[Note](./622/note.md)|Medium|O(n)|O(n)||
|No.641|[Design Circular Deque](https://leetcode.com/problems/design-circular-deque/)|[Solution](./641/Solution.py)|[Note](./641/note.md)|Medium|O(n)|O(n)||
|No.933|[Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)|[Solution](./933/Solution.py)|[Note](./933/note.md)|Easy|O(n)|O(n)||


## Binary Tree
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.226|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)|[Solution](./226/Solution.py)|[Note](./226/note.md)|Easy|O(logn)|O(h)||
|No.538|[Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)|[Solution](./538/Solution.py)|[Note](./538/note.md)|Easy|O(n)|O(h)||
|No.543|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)|[Solution](./543/Solution.py)|[Note](./543/note.md)|Easy|O(n)|O(h)||
|No.687|[Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)|[Solution](./687/Solution.py)|[Note](./687/note.md)|Easy|O(n)|O(h)||
|No.897|[Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)|[Solution](./897/Solution.py)|[Note](./897/note.md)|Easy|O(n)|O(h)||
|No.617|[Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)|[Solution](./617/Solution.py)|[Note](./617/note.md)|Easy|O(n)|O(h)||
|No.606|[Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)|[Solution](./606/Solution.py)|[Note](./606/note.md)|Easy|O(n)|O(h)||
|No.572|[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)|[Solution](./572/Solution.py)|[Note](./572/note.md)|Easy|O(n)|O(h)||
|No.563|[Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt/)|[Solution](./563/Solution.py)|[Note](./563/note.md)|Easy|O(n^2)|||
|No.094|[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|[Solution](./094/Solution.py)|[Note](./094/note.md)|Medium|O(n)|O(n)|Inorder Traversal|
|No.112|[Path Sum](https://leetcode.com/problems/path-sum/)|[Solution](./112/Solution.py)|[Note](./112/note.md)|Easy|O(n)|O(1)|DFS|
|No.257|[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)|[Solution](./257/Solution.py)|[Note](./257/note.md)|Easy|O(n)|O(1)|DFS|
|No.144|[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)|[Solution](./144/Solution.py)|[Note](./144/note.md)|Medium|O(n)|O(n)|iteration traverse|
|No.145|[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)|[Solution](./145/Solution.py)|[Note](./145/note.md)|Hard|O(n)|O(n)|iteration traverse|
|No.102|[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|[Solution](./102/Solution.py)|[Note](./102/note.md)|Medium|O(n)|O(n)|iteration traverse|
|No.250|[Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees/)|[Solution](./250/Solution.py)|[Note](./250/note.md)|Medium|O(n)|O(n)||
|No.106|[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)|[Solution](./106/Solution.py)|[Note](./106/note.md)|Medium|O(n)|O(n)|build tree|
|No.105|[Construct Binary Tree from Inorder and Preorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|[Solution](./105/Solution.py)|[Note](./105/note.md)|Medium|O(n)|O(n)|build tree|
|No.116|[Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|[Solution](./116/Solution.py)|[Note](./116/note.md)|Medium|O(n)|O(n)||
|No.117|[Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)|[Solution](./117/Solution.py)|[Note](./117/note.md)|Medium|O(n)|O(n)||
|No.236|[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)|[Solution](./236/Solution.py)|[Note](./236/note.md)|Medium|O(n^2)|O(n)||
|No.100|[Same Tree](https://leetcode.com/problems/same-tree/)|[Solution](./100/Solution.py)|[Note](./100/note.md)|Medium|O(n)|O(1)||
|No.314|Binary Tree Vertical Order Traversal|[Solution](./314/Solution.py)|[Note](./314/note.md)|Medium|O(n)|O(n)||
|No.637|[Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)|[Solution](./637/Solution.py)|[Note](./637/note.md)|Easy|O(n)|O(n)||
|No.103|[Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)|[Solution](./103/Solution.py)|[Note](./103/note.md)|Medium|O(n)|O(n)||
|No.114|Flatten Binary Tree to Linked List|[Solution](./114/Solution.py)|[Note](./114/note.md)|Medium|O(n)|O(1)|DFS|
|No.437|[Path Sum III](https://leetcode.com/problems/path-sum-iii/)|[Solution](./437/Solution.py)|[Note](./437/note.md)|Medium|O(nlogn)|O(1)|DFS|
|No.965|[Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/)|[Solution](./965/Solution.py)|[Note](./965/note.md)|Easy|O(n)|O(1)||
|No.1022|[Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)|[Solution](./1022/Solution.py)|[Note](./1022/note.md)|Easy|O(n)|O(1)||
|No.993|[Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/)|[Solution](./993/Solution.py)|[Note](./993/note.md)|Easy|O(n)|O(1)||
|No.107|[Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)|[Solution](./107/Solution.py)|[Note](./107/note.md)|Easy|O(n)|O(n)||
|No.654|[Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)|[Solution](./654/Solution.py)|[Note](./654/note.md)|Medium|O(nlogn)|O(n)||
|No.1008|[Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)|[Solution](./1008/Solution.py)|[Note](./1008/note.md)|Medium|O(nlogn)|O(n)||
|No.701|[Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)|[Solution](./701/Solution.py)|[Note](./701/note.md)|Medium|O(logn)|O(n)||
|No.814|[Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)|[Solution](./814/Solution.py)|[Note](./814/note.md)|Medium|O(logn)|O(n)||
|No.655|[Print Binary Tree](https://leetcode.com/problems/print-binary-tree/)|[Solution](./655/Solution.py)|[Note](./655/note.md)|Medium|O(n)|O(n)||
|No.988|[Maximum Binary Tree II](https://leetcode.com/problems/maximum-binary-tree-ii/)|[Solution](./988/Solution.py)|[Note](./988/note.md)|Medium|O(n)|O(n)||
|No.1123|[Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)|[Solution](./1123/Solution.py)|[Note](./1123/note.md)|Medium|O(n)|O(n)||
|No.199|[Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)|[Solution](./199/Solution.py)|[Note](./199/note.md)|Medium|O(n)|O(n)||
|No.1305|[All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)|[Solution](./1305/Solution.py)|[Note](./1305/note.md)|Medium|O(n)|O(n)||
|No.1382|[Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/)|[Solution](./1382/Solution.py)|[Note](./1382/note.md)|Medium|O(n)|O(n)||
|No.1038|[Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)|[Solution](./1038/Solution.py)|[Note](./1038/note.md)|Medium|O(n)|O(n)||
|No.652|[Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/)|[Solution](./652/Solution.py)|[Note](./652/note.md)|Medium|O(n)|O(n)||
|No.1261|[FFind Elements in a Contaminated Binary Tree](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/)|[Solution](./1261/Solution.py)|[Note](./1261/note.md)|Medium|O(n)|O(n)||
|No.124|[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)|[Solution](./124/Solution.py)|[Note](./124/note.md)|hard|O(n)|O(1)||

## Hash Table
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.202|[Happy Number](https://leetcode.com/problems/happy-number/)|[Solution](./202/Solution.py)|[Note](./202/note.md)|Easy|O(n)|O(n)||
|No.204|[Count Primes](https://leetcode.com/problems/count-primes/)|[Solution](./204/Solution.py)|[Note](./204/note.md)|Easy|O(n)|||
|No.205|Isomorphic Strings|[Solution](./205/Solution.py)|[Note](./205/note.md)|Easy|O(n)|O(n)||
|No.217|Contains Duplicate|[Solution](./217/Solution.py)|[Note](./217/note.md)|Easy|O(n)|O(n)||
|No.219|Contains DuplicateII|[Solution](./219/Solution.py)|[Note](./219/note.md)|Easy|O(n)|O(n)||
|No.246|Strobogrammatic Number|[Solution](./246/Solution.py)|[Note](./246/note.md)|Easy|O(n)|O(n)||
|No.244|Shortest Word Distance II|[Solution](./244/Solution.py)|[Note](./244/note.md)|Medium|O(m+n)|O(n)||
|No.249|Group Shifted Strings|[Solution](./249/Solution.py)|[Note](./249/note.md)|Easy|O(n)|O(n)||
|No.266|Palindrome Permutation|[Solution](./266/Solution.py)|[Note](./266/note.md)|Easy|O(n)|O(n)||
|No.288|Unique Word Abbreviation|[Solution](./288/Solution.py)|[Note](./288/note.md)|Medium|O(n)|O(n)||
|No.299|Bulls and Cows|[Solution](./299/Solution.py)|[Note](./299/note.md)|Medium|O(n)|O(n)||
|No.387|First Unique Character in a String|[Solution](./387/Solution.py)|[Note](./387/note.md)|Easy|O(n)|O(n)||
|No.350|Intersection of Two Arrays II|[Solution](./350/Solution.py)|[Note](./350/note.md)|Easy|O(n)|O(n)||
|No.049|[Group Anagrams](https://leetcode.com/problems/group-anagrams/)|[Solution](./049/Solution.py)|[Note](./049/note.md)|Medium|O(nklonk)|O(n)||
|No.705|Design HashSet |[Solution](./705/Solution.py)|[Note](./705/note.md)|Easy|O(1)|O(n)||
|No.599|Minimum Index Sum of Two Lists|[Solution](./599/Solution.py)|[Note](./599/note.md)|Easy|O(1)|O(n)||
|No.359|Logger Rate Limiter|[Solution](./359/Solution.py)|[Note](./359/note.md)|Easy|O(1)|O(n)||
|No.706|[Design HashMap](https://leetcode.com/problems/design-hashmap/)|[Solution](./706/Solution.py)|[Note](./706/note.md)|Easy|O(1)|O(n)||
|No.380|[ Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)|[Solution](./380/Solution.py)|[Note](./380/note.md)|Medium|O(1)|O(n)||
|No.981|[ Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)|[Solution](./981/Solution.py)|[Note](./981/note.md)|Medium|O(nlogn)|O(n)||
|No.811|[ Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/)|[Solution](./811/Solution.py)|[Note](./811/note.md)|Easy|O(nm)|O(n)||
|No.609|[ Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/)|[Solution](./609/Solution.py)|[Note](./609/note.md)|Medium|O(nk)|O(n)||
|No.692|[Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)|[Solution](./692/Solution.py)|[Note](./692/note.md)|Medium|O(nlogn)|O(n)||
|No.1119|[Remove Vowels from a String](https://leetcode.com/problems/remove-vowels-from-a-string/)|[Solution](./1119/Solution.py)|[Note](./1119/note.md)|Easy|O(n)|O(1)||
|No.1165|[Single-Row Keyboard](https://leetcode.com/problems/single-row-keyboard/)|[Solution](./1165/Solution.py)|[Note](./1165/note.md)|Easy|O(n)|O(1)||
|No.760|[Find Anagram Mappings](https://leetcode.com/problems/find-anagram-mappings/)|[Solution](./760/Solution.py)|[Note](./760/note.md)|Easy|O(n)|O(n)||
|No.804|[Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/)|[Solution](./804/Solution.py)|[Note](./804/note.md)|Easy|O(n)|O(n)||
|No.1252|[Cells with Odd Values in a Matrix](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/)|[Solution](./1252/Solution.py)|[Note](./1252/note.md)|Easy|O(n^2)|O(n)||
|No.954|[Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/)|[Solution](./954/Solution.py)|[Note](./954/note.md)|Easy|O(n)|O(n)||
|No.146|[LRU Cache](https://leetcode.com/problems/lru-cache/)|[Solution](./146/Solution.py)|[Note](./146/note.md)|Medium|O(n)|O(n)||


## Sort
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.088|Merge Sorted Array|[Solution](./088/Solution.py)|[Note](./088/note.md)|Medium|O(n+m)|O(1)|three pointer|
|No.252|Meeting Room|[Solution](./252/Solution.py)|[Note](./252/note.md)|Easy|O(nlogn)|O(1)||
|No.075|Sort Colors|[Solution](./075/Solution.py)|[Note](./075/note.md)|Medium|O(n)|O(1)|tri pointer|
|No.147|Insertion Sort List|[Solution](./147/Solution.py)|[Note](./147/note.md)|Medium|O(n^2)|O(1)||
|No.148|Sort List|[Solution](./148/Solution.py)|[Note](./148/note.md)|Medium|O(nlog)|O(1)|list merge sort|
|No.179|[Largest Number](https://leetcode.com/problems/largest-number/)|[Solution](./179/Solution.py)|[Note](./179/note.md)|Medium|O(nlogn)|O(1)|cmp_to_key|
|No.253|Meeting Rooms II|[Solution](./253/Solution.py)|[Note](./253/note.md)|Medium|O(nlogn)|O(n)||
|No.347|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)|[Solution](./347/Solution.py)|[Note](./347/note.md)|Medium|O(nlogn)|O(n)||
|No.581|[Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)|[Solution](./581/Solution.py)|[Note](./581/note.md)|Easy|O(n)|O(1)||
|No.1051|Height Checker|[Solution](./1051/Solution.py)|[Note](./1051/note.md)|Easy|O(nlogn)|O(n)||
|No.207|[Course Schedule](https://leetcode.com/problems/course-schedule/)|[Solution](./207/Solution.py)|[Note](./207/note.md)|Meduim|O(n)|O(n)||
|No.912|[Sort an Array](https://leetcode.com/problems/sort-an-array/)|[Solution](./912/Solution.py)|[Note](./912/note.md)|Meduim|O(nlogn)|O(n)||
|No.406|[Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)|[Solution](./406/Solution.py)|[Note](./406/note.md)|Meduim|O(nlogn)|O(n)||


## Heap
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.264|[Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)|[Solution](./264/Solution.py)|[Note](./264/note.md)|Medium|O(n)|O(1)||
|No.313|Super Ugly Number|[Solution](./313/Solution.py)|[Note](./313/note.md)|Medium|O(n * k)|O(n * k)||
|No.378|Kth Smallest Element in a Sorted Matrix|[Solution](./378/Solution.py)|[Note](./378/note.md)|Medium|O(nklogn)|O(n)||
|No.215|[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)|[Solution](./215/Solution.py)|[Note](./215/note.md)|Medium|O(n+klogn)|O(n)||
|No.937|[K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)|[Solution](./937/Solution.py)|[Note](./937/note.md)|Medium|O(klogn)|O(n)||
|No.239|[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)|[Solution](./239/Solution.py)|[Note](./239/note.md)|Hard|O(nlogk)|O(n)||
|No.1046|[Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)|[Solution](./1046/Solution.py)|[Note](./1046/note.md)|Easy|O(nlogn)|O(n)||


## Binary Search
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.855|Exam Room|[Solution](./855/Solution.py)|[Note](./855/note.md)|Medium|O(n)|O(n)||
|No.374|Guess Number Higher or Lower|[Solution](./374/Solution.py)|[Note](./374/note.md)|Easy|O(logn)|O(1)||
|No.475|Heaters|[Solution](./475/Solution.py)|[Note](./475/note.md)|Easy|O(nlogn)|O(1)||
|No.744|Find Smallest Letter Greater Than Target|[Solution](./744/Solution.py)|[Note](./744/note.md)|Easy|O(n)|O(1)||
|No.852|Peak Index in a Mountain Array|[Solution](./852/Solution.py)|[Note](./852/note.md)|Easy|O(n)|O(1)||
|No.050|[Pow(x, n)](https://leetcode.com/problems/powx-n/)|[Solution](./050/Solution.py)|[Note](./050/note.md)|Medium|O(logn)|O(1)||
|No.153|[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)|[Solution](./153/Solution.py)|[Note](./153/note.md)|Medium|O(logn)|O(n)||
|No.704|[Binary Search](https://leetcode.com/problems/binary-search/)|[Solution](./704/Solution.py)|[Note](./704/note.md)|Easy|O(logn)|O(1)||
|No.1201|[Ugly Number III](https://leetcode.com/problems/ugly-number-iii/)|[Solution](./1201/Solution.py)|[Note](./1201/note.md)|Medium|O(logn)|O(1)||
|No.074|[Search a 2D Matrix](https://leetcode-cn.com/problems/search-a-2d-matrix/)|[Solution](./074/Solution.py)|[Note](./074/note.md)|Medium|O(logn)|O(1)||
|No.162|[Find Peak Element](https://leetcode-cn.com/problems/find-peak-element/)|[Solution](./162/Solution.py)|[Note](./162/note.md)|Medium|O(logn)|O(1)||


## Binary Search Tree
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.235|[Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)|[Solution](./235/Solution.py)|[Note](./235/note.md)|Easy|O(logn)|O(1)||
|No.270|[Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/)|[Solution](./270/Solution.py)|[Note](./270/note.md)|Easy|O(logn)|O(1)||
|No.653|[Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)|[Solution](./653/Solution.py)|[Note](./653/note.md)|Easy|O(n)|O(n)||
|No.098|Validate Binary Search Tree|[Solution](./098/Solution.py)|[Note](./098/note.md)|Easy|O(n)|O(n)||
|No.278|First Bad Version|[Solution](./278/Solution.py)|[Note](./278/note.md)|Easy|O(logn)|O(1)||
|No.033|[Search in Rotated Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|[Solution](./033/Solution.py)|[Note](./033/note.md)|Medium|O(logn)|O(1)||
|No.173|Binary Search Tree Iterator|[Solution](./173/Solution.py)|[Note](./173/note.md)|Medium|O(1)|O(h)||
|No.938|[Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)|[Solution](./938/Solution.py)|[Note](./938/note.md)|Easy|O(n)|O(1)||
|No.700|[Search in a Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)|[Solution](./700/Solution.py)|[Note](./700/note.md)|Easy|O(n)|O(1)||
|No.108|[Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)|[Solution](./108/Solution.py)|[Note](./108/note.md)|Easy|O(n)|O(1)||
|No.530|[Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)|[Solution](./530/Solution.py)|[Note](./530/note.md)|Easy|O(n)|O(1)||
|No.783|[Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)|[Solution](./783/Solution.py)|[Note](./783/note.md)|Easy|O(n)|O(1)||
|No.501|[Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)|[Solution](./501/Solution.py)|[Note](./501/note.md)|Easy|O(n)|O(n)||
|No.776|[Split BST](https://leetcode.com/problems/split-bst/)|[Solution](./776/Solution.py)|[Note](./776/note.md)|Medium|O(logn)|O(n)||
|No.426|[Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)|[Solution](./426/Solution.py)|[Note](./426/note.md)|Medium|O(n)|O(1)||
|No.230|[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)|[Solution](./230/Solution.py)|[Note](./230/note.md)|Medium|O(n)|O(1)||


## N-ary Tree
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.589|[N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)|[Solution](./589/Solution.py)|[Note](./589/note.md)|Easy|O(n)|O(n)||
|No.590|[N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)|[Solution](./590/Solution.py)|[Note](./590/note.md)|Easy|O(n)|O(n)||
|No.429|[N-ary Tree Levelorder Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)|[Solution](./429/Solution.py)|[Note](./429/note.md)|Easy|O(n)|O(n)||
|No.559|[Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|[Solution](./559/Solution.py)|[Note](./559/note.md)|Easy|O(n)|O(n)||
|No.208|Implement Trie (Prefix Tree)|[Solution](./208/Solution.py)|[Note](./208/note.md)|Medium|O(k)|O(n)|trie|
|No.677|Map Sum Pairs|[Solution](./677/Solution.py)|[Note](./677/note.md)|Medium|||trie|
|No.648|Replace Words|[Solution](./648/Solution.py)|[Note](./648/note.md)|Medium|O(n)|O(n)|trie|
|No.211|[Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/)|[Solution](./211/Solution.py)|[Note](./211/note.md)|Medium|O(n)|O(n)|trie|
|No.1233|[Remove Sub-Folders from the Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/)|[Solution](./1233/Solution.py)|[Note](./1233/note.md)|Medium|O(n)|O(n)|trie|
|No.720|[Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)|[Solution](./720/Solution.py)|[Note](./720/note.md)|Easy|O(n^2)|O(n)|trie|


## Math
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.263|Ugly Number|[Solution](./263/Solution.py)|[Note](./263/note.md)|Easy|O(n)|O(1)||
|No.238|[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)|[Solution](./238/Solution.py)|[Note](./238/note.md)|Medium|O(n)|O(n)||
|No.621|Task Scheduler|[Solution](./621/Solution.py)|[Note](./621/note.md)|Medium|O(n)|O(1)||
|No.326|Power of Three|[Solution](./326/Solution.py)|[Note](./326/note.md)|Easy|O(n)|O(1)||
|No.892|Surface Area of 3D Shapes|[Solution](./892/Solution.py)|[Note](./892/note.md)|Easy|O(n)|O(1)||
|No.1266|[Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)|[Solution](./1266/Solution.py)|[Note](./1266/note.md)|Easy|O(n)|O(1)||
|No.1281|[Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)|[Solution](./1281/Solution.py)|[Note](./1281/note.md)|Easy|O(n)|O(n)||
|No.1232|[Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)|[Solution](./1232/Solution.py)|[Note](./1232/note.md)|Easy|O(n)|O(1)||
|No.258|[Add Digits](https://leetcode.com/problems/add-digits/)|[Solution](./258/Solution.py)|[Note](./258/note.md)|Easy|O(n)|O(n)||
|No.069|[Sqrt(x)](https://leetcode.com/problems/sqrtx/)|[Solution](./069/Solution.py)|[Note](./069/note.md)|Easy|O(n)|O(1)||
|No.1033|[Moving Stones Until Consecutive](https://leetcode.com/problems/moving-stones-until-consecutive/)|[Solution](./1033/Solution.py)|[Note](./1033/note.md)|Easy|O(1)|O(1)||
|No.1342|[Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)|[Solution](./1342/Solution.py)|[Note](./1342/note.md)|Easy|O(n)|O(1)||
|No.504|[Base 7](https://leetcode.com/problems/base-7/)|[Solution](./504/Solution.py)|[Note](./504/note.md)|Easy|O(n)|O(1)||
|No.470|[Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/)|[Solution](./470/Solution.py)|[Note](./470/note.md)|medium|O(1)|O(1)||
|No.154|[Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)|[Solution](./154/Solution.py)|[Note](./154/note.md)|hard|O(n)|O(1)||
|No.007|[Reverse Integer](https://leetcode-cn.com/problems/reverse-integer/)|[Solution](./007/Solution.py)|[Note](./007/note.md)|Medium|O(1)|O(1)||


## Graph
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|



## Backtracking
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.017|[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|[Solution](./017/Solution.py)|[Note](./017/note.md)|Medium|O(n)|O(n)||
|No.093|[Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)|[Solution](./093/Solution.py)|[Note](./093/note.md)|Medium|O(n^4)|O(n)||
|No.078|[Subset](https://leetcode.com/problems/subsets/)|[Solution](./078/Solution.py)|[Note](./078/note.md)|Medium|O(2^n)|O(n)||
|No.078|[SubsetII](https://leetcode.com/problems/subsets-ii/)|[Solution](./090/Solution.py)|[Note](./090/note.md)|Medium|O(2^n)|O(n)||
|No.046|[Permutations](https://leetcode.com/problems/permutations/)|[Solution](./046/Solution.py)|[Note](./046/note.md)|Medium|O(n!)|O(n)||
|No.047|[PermutationsII](https://leetcode.com/problems/permutations-ii/)|[Solution](./047/Solution.py)|[Note](./047/note.md)|Medium|O(n!)|O(n)||
|No.079|[Word Search](https://leetcode.com/problems/word-search/)|[Solution](./079/Solution.py)|[Note](./079/note.md)|Medium|O(n^2)|O(n)||
|No.022|Generate Parentheses|[Solution](./022/Solution.py)|[Note](./022/note.md)|Medium|O(n!)|O(n)||
|No.039|[Combination Sum](https://leetcode.com/problems/combination-sum/)|[Solution](./039/Solution.py)|[Note](./039/note.md)|Medium|O(n!)|O(n)||
|No.784|[Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)|[Solution](./784/Solution.py)|[Note](./784/note.md)|Easy|O(n*2)|O(n) + O(n*2)||
|No.1079|[Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities/)|[Solution](./1079/Solution.py)|[Note](./1079/note.md)|Easy|O(2*n)|O(2*n)||
|No.077|[Combinations](https://leetcode.com/problems/combinations/)|[Solution](./077/Solution.py)|[Note](./077/note.md)|Medium|O(2^n)|O(2^n)||
|No.040|[Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)|[Solution](./040/Solution.py)|[Note](./040/note.md)|Medium|O(n^n)|O(n^n)||
|No.695|[Max Area of Island](https://leetcode.com/problems/max-area-of-island/)|[Solution](./695/Solution.py)|[Note](./695/note.md)|Medium|O(n^2)|O(n^2)||

## BFS
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.200|[Number of Islands](https://leetcode.com/problems/number-of-islands/)|[Solution](./200/Solution.py)|[Note](./200/note.md)|Medium|O(n)|O(n)|BFS|
|No.133|Clone Graph|[Solution](./133/Solution.py)|[Note](./133/note.md)|Medium|O(n)|O(n)|BFS|
|No.1162|[As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/)|[Solution](./1162/Solution.py)|[Note](./1162/note.md)|Medium|O(n)|O(n)|BFS|



## DFS
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.1145|[Binary Tree Coloring Game](https://leetcode.com/problems/binary-tree-coloring-game/)|[Solution](./1145/Solution.py)|[Note](./1145/note.md)|Medium|O(n)|O(1)||
|No.863|[All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)|[Solution](./863/Solution.py)|[Note](./863/note.md)|Medium|O(n)|O(n)||
|No.1034|[Coloring A Border](https://leetcode.com/problems/coloring-a-border/)|[Solution](./1034/Solution.py)|[Note](./1034/note.md)|Medium|O(n)|O(n)||
|No.306|[Additive Number](https://leetcode.com/problems/additive-number/)|[Solution](./306/Solution.py)|[Note](./306/note.md)|Medium|O(n^2)|O(n)||
|No.842|[Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)|[Solution](./842/Solution.py)|[Note](./842/note.md)|Medium|O(n^2)|O(n)||
|No.399|Evaluate Division|[Solution](./399/Solution.py)|[Note](./399/note.md)|Medium|O(n)|O(n)|DFS|
|No.526|[Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)|[Solution](./526/Solution.py)|[Note](./526/note.md)|Medium|O(n!)|O(n)|DFS|
|No.733|[Flood Fill](https://leetcode.com/problems/flood-fill/)|[Solution](./733/Solution.py)|[Note](./733/note.md)|Easy|O(n^2)|O(1)||

## Greedy
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.455|[Assign Cookies](https://leetcode.com/problems/assign-cookies/)|[Solution](./455/Solution.py)|[Note](./455/note.md)|Easy|O(nlogn)|O(1)||
|No.055|[Jump Game](https://leetcode.com/problems/jump-game/)|[Solution](./055/Solution.py)|[Note](./055/note.md)|Medium|O(n)|O(1)||
|No.2086|[Minimum Number of Buckets Required to Collect Rainwater from Houses](https://leetcode-cn.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/)|[Solution](./2086/Solution.py)|[Note](./2086/note.md)|Medium|O(n)|O(1)||

## Divide and Conquer
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.932|[Beautiful Array](https://leetcode.com/problems/beautiful-array/)|[Solution](./932/Solution.py)|[Note](./932/note.md)|Medium|O(nlogn)|O(n)||
|No.241|[Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)|[Solution](./241/Solution.py)|[Note](./241/note.md)|Medium|O(nlogn)|O(n)||


## Dynamic Programming
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.091|Decode Ways|[Solution](./091/Solution.py)|[Note](./091/note.md)|Medium|O(n)|O(1)||
|No.062|[Unique Paths](https://leetcode.com/problems/unique-paths/)|[Solution](./062/Solution.py)|[Note](./062/note.md)|Medium|O(n^2)|O(n)||
|No.070|Combing Stairs|[Solution](./070/Solution.py)|[Note](./070/note.md)|Medium|O(n)|O(n)||
|No.926|Flip String to Monotone Increasing|[Solution](./926/Solution.py)|[Note](./926/note.md)|Medium|O(n)|O(n)||
|No.845|Longest Mountain in Array|[Solution](./845/Solution.py)|[Note](./845/note.md)|Medium|O(n)|O(1)||
|No.139|Longest Mountain in Array|[Solution](./139/Solution.py)|[Note](./139/note.md)|Medium|O(n)|O(1)||
|No.300|Longest Increasing Subsequence|[Solution](./300/Solution.py)|[Note](./300/note.md)|Medium|O(nlogn)|O(1)||
|No.198|[House Robber](https://leetcode.com/problems/house-robber/)|[Solution](./198/Solution.py)|[Note](./198/note.md)|Easy|O(n)|O(n)||
|No.213|[House Robber II](https://leetcode-cn.com/problems/house-robber-ii/)|[Solution](./213/Solution.py)|[Note](./213/note.md)|Medium|O(n)|O(n)||
|No.746|[Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)|[Solution](./746/Solution.py)|[Note](./746/note.md)|Easy|O(n)|O(n)||
|No.790|[Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/)|[Solution](./790/Solution.py)|[Note](./790/note.md)|Medium|O(n)|O(n)||
|No.801|[Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/)|[Solution](./801/Solution.py)|[Note](./801/note.md)|Medium|O(n)|O(n)||
|No.718|[Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)|[Solution](./718/Solution.py)|[Note](./718/note.md)|Medium|O(n*m)|O(n*m)||
|No.1143|[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)|[Solution](./1143/Solution.py)|[Note](./1143/note.md)|Medium|O(n*m)|O(n*m)||
|No.583|[Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)|[Solution](./583/Solution.py)|[Note](./583/note.md)|Medium|O(n*m)|O(n*m)||
|No.1092|[Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)|[Solution](./1092/Solution.py)|[Note](./1092/note.md)|Hard|O(n*m)|O(n*m)||
|No.032|[Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)|[Solution](./032/Solution.py)|[Note](./032/note.md)|Hard|O(n)|O(n)||
|No.152|[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)|[Solution](./152/Solution.py)|[Note](./152/note.md)|Medium|O(n)|O(1)||
|No.647|[Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)|[Solution](./647/Solution.py)|[Note](./647/note.md)|Medium|O(n^2)|O(1)||
|No.416|[Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)|[Solution](./416/Solution.py)|[Note](./416/note.md)|Medium|O(n^2)|O(n)||
|No.279|[Perfect Squares](https://leetcode.com/problems/perfect-squares/)|[Solution](./279/Solution.py)|[Note](./279/note.md)|Medium|O(n^2)|O(n)||
|No.418|[Sentence Screen Fitting](https://leetcode-cn.com/problems/sentence-screen-fitting/)|[Solution](./418/Solution.py)|[Note](./418/note.md)|Medium|O(n^2)|O(n)||
|No.070|[Climbing Stairs](https://leetcode-cn.com/problems/climbing-stairs/)|[Solution](./070/Solution.py)|[Note](./070/note.md)|Medium|O(n)|O(n)||
|No.6305|[Climbing Stairs](https://leetcode-cn.com/problems/number-of-ways-to-select-buildings/)|[Solution](./6305/Solution.py)|[Note](./6305/note.md)|Medium|O(n)|O(1)||
|No.322|[Coin Change](https://leetcode-cn.com/problems/coin-change/)|[Solution](./322/Solution.py)|[Note](./322/note.md)|Medium|O(n)|O(1)||
|No.064|[Minimum Path Sum](https://leetcode-cn.com/problems/minimum-path-sum/)|[Solution](./064/Solution.py)|[Note](./064/note.md)|Medium|O(n*m)|O(m*n)||
|No.343|[Integer Break](https://leetcode-cn.com/problems/integer-break/)|[Solution](./343/Solution.py)|[Note](./343/note.md)|Medium|O(n^2)|O(n)||



## Design
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.1063|[Design Parking System](https://leetcode-cn.com/problems/design-parking-system/)|[Solution](./1063/Solution.py)|[Note](./1063/note.md)|Easy|O(n)|O(1)||


## SQL Schema
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.1068|[Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i/)|[Solution](./1068/Solution.py)|[Note](./1068/note.md)|Easy|O(n*n)|O(n*n)||
|No.1069|[Product Sales Analysis II](https://leetcode.com/problems/product-sales-analysis-ii/)|[Solution](./1069/Solution.py)|[Note](./1069/note.md)|Easy|O(n)|O(n)||
|No.511|[Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/)|[Solution](./511/Solution.py)|[Note](./511/note.md)|Easy|O(n)|O(n)||
|No.595|[Big Countries](https://leetcode.com/problems/big-countries/)|[Solution](./595/Solution.py)|[Note](./595/note.md)|Easy|O(n)|O(n)||
|No.1173|[Immediate Food Delivery I](https://leetcode.com/problems/immediate-food-delivery-i/)|[Solution](./1173/Solution.py)|[Note](./1173/note.md)|Easy|O(n)|O(n)||
|No.613|[Shortest Distance in a Line](https://leetcode.com/problems/shortest-distance-in-a-line/)|[Solution](./613/Solution.py)|[Note](./613/note.md)|Easy|O(n)|O(n)||
|No.1050|[Actors and Directors Who Cooperated At Least Three Times](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/)|[Solution](./1050/Solution.py)|[Note](./1050/note.md)|Easy|O(n)|O(n)||
|No.627|[Swap Salary](https://leetcode.com/problems/swap-salary/)|[Solution](./627/Solution.py)|[Note](./627/note.md)|Easy|O(n)|O(1)||
|No.1082|[Sales Analysis I](https://leetcode.com/problems/sales-analysis-i/)|[Solution](./1082/Solution.py)|[Note](./1082/note.md)|Easy|O(n)|O(1)||
|No.620|[Not Boring Movies](https://leetcode.com/problems/not-boring-movies/)|[Solution](./620/Solution.py)|[Note](./620/note.md)|Easy|O(n)|O(1)||



## 剑指offer
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.LZOF_03|[数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)|[Solution](./LZOF_03/Solution.py)|[Note](./LZOF_03/note.md)|Easy|O(n)|O(1)||
|No.LZOF_04|[二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)|[Solution](./LZOF_04/Solution.py)|[Note](./LZOF_04/note.md)|Easy|O(nlogn)|O(1)||
|No.LZOF_05|[替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)|[Solution](./LZOF_05/Solution.py)|[Note](./LZOF_05/note.md)|Easy|O(n)|O(n)||
|No.LZOF_06|[从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)|[Solution](./LZOF_06/Solution.py)|[Note](./LZOF_06/note.md)|Easy|O(n)|O(n)||
|No.LZOF_07|[重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)|[Solution](./LZOF_07/Solution.py)|[Note](./LZOF_07/note.md)|Medium|O(n)|O(n)||
|No.LZOF_09|[用两个栈实现队列  ](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)|[Solution](./LZOF_09/Solution.py)|[Note](./LZOF_09/note.md)|Easy|O(n)|O(n)||
|No.LZOF_10|[斐波那契数列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)|[Solution](./LZOF_10/Solution.py)|[Note](./LZOF_10/note.md)|Easy|O(n)|O(n)||
|No.LZOF_10-2|[青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)|[Solution](./LZOF_10-2/Solution.py)|[Note](./LZOF_10-2/note.md)|Easy|O(n)|O(n)||
|No.LZOF_11|[旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)|[Solution](./LZOF_11/Solution.py)|[Note](./LZOF_11/note.md)|Easy|O(n)|O(1)||
|No.LZOF_12|[矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)|[Solution](./LZOF_12/Solution.py)|[Note](./LZOF_12/note.md)|Medium|O(n*2)|O(n)||
|No.LZOF_13|[机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)|[Solution](./LZOF_13/Solution.py)|[Note](./LZOF_13/note.md)|Medium|O(n*2)|O(n)||
|No.LZOF_14|[剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)|[Solution](./LZOF_14/Solution.py)|[Note](./LZOF_14/note.md)|Medium|O(n*2)|O(n)||
|No.LZOF_14_II|[剪绳子II](https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/)|[Solution](./LZOF_14_II/Solution.py)|[Note](./LZOF_14_II/note.md)|Medium|O(n*2)|O(n)||
|No.LZOF_15|[二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)|[Solution](./LZOF_15/Solution.py)|[Note](./LZOF_15/note.md)|Medium|O(n)|O(1)||
|No.LZOF_16|[数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)|[Solution](./LZOF_16/Solution.py)|[Note](./LZOF_16/note.md)|Medium|O(logn)|O(1)||
|No.LZOF_17|[打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)|[Solution](./LZOF_17/Solution.py)|[Note](./LZOF_17/note.md)|Easy|O(n)|O(n)||
|No.LZOF_18|[删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)|[Solution](./LZOF_18/Solution.py)|[Note](./LZOF_18/note.md)|Easy|O(n)|O(n)||
|No.LZOF_19|[正则表达式匹配](https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/)|[Solution](./LZOF_19/Solution.py)|[Note](./LZOF_19/note.md)|Hard|O(nm)|O(nm)||
|No.LZOF_21|[调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)|[Solution](./LZOF_21/Solution.py)|[Note](./LZOF_21/note.md)|Easy|O(n)|O(1)||
|No.LZOF_22|[链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)|[Solution](./LZOF_22/Solution.py)|[Note](./LZOF_22/note.md)|Easy|O(n)|O(1)||
|No.LZOF_24|[反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)|[Solution](./LZOF_24/Solution.py)|[Note](./LZOF_24/note.md)|Easy|O(n)|O(1)||
|No.LZOF_25|[合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)|[Solution](./LZOF_25/Solution.py)|[Note](./LZOF_25/note.md)|Easy|O(n)|O(1)||
|No.LZOF_26|[树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)|[Solution](./LZOF_26/Solution.py)|[Note](./LZOF_26/note.md)|Easy|O(n^2)|O(1)||
|No.LZOF_27|[二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)|[Solution](./LZOF_27/Solution.py)|[Note](./LZOF_27/note.md)|Easy|O(n)|O(1)||
|No.LZOF_28|[对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)|[Solution](./LZOF_28/Solution.py)|[Note](./LZOF_28/note.md)|Easy|O(n)|O(1)||
|No.LZOF_29|[顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)|[Solution](./LZOF_29/Solution.py)|[Note](./LZOF_29/note.md)|Easy|O(n)|O(n)||
|No.LZOF_30|[包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)|[Solution](./LZOF_30/Solution.py)|[Note](./LZOF_30/note.md)|Easy|O(1)|O(1)||
|No.LZOF_31|[ 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)|[Solution](./LZOF_31/Solution.py)|[Note](./LZOF_31/note.md)|Medium|O(n)|O(n)||
|No.LZOF_32|[从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)|[Solution](./LZOF_32/Solution.py)|[Note](./LZOF_32/note.md)|Medium|O(n)|O(n)||
|No.LZOF_32_II|[从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)|[Solution](./LZOF_32_II/Solution.py)|[Note](./LZOF_32_II/note.md)|Medium|O(n)|O(n)||
|No.LZOF_32_III|[从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)|[Solution](./LZOF_32_III/Solution.py)|[Note](./LZOF_32_III/note.md)|Medium|O(n)|O(n)||
|No.LZOF_33|[二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)|[Solution](./LZOF_33/Solution.py)|[Note](./LZOF_33/note.md)|Medium|O(n)|O(n)||
|No.LZOF_34|[二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)|[Solution](./LZOF_34/Solution.py)|[Note](./LZOF_34/note.md)|Medium|O(n)|O(n)||
|No.LZOF_35|[复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/)|[Solution](./LZOF_35/Solution.py)|[Note](./LZOF_35/note.md)|Medium|O(n)|O(n)||
|No.LZOF_36|[二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)|[Solution](./LZOF_36/Solution.py)|[Note](./LZOF_36/note.md)|Medium|O(n)|O(1)||
|No.LZOF_37|[序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)|[Solution](./LZOF_37/Solution.py)|[Note](./LZOF_37/note.md)|Hard|O(n)|O(n)||
|No.LZOF_38|[字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)|[Solution](./LZOF_38/Solution.py)|[Note](./LZOF_38/note.md)|Medium|O(n!)|O(n)||
|No.LZOF_39|[数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)|[Solution](./LZOF_39/Solution.py)|[Note](./LZOF_39/note.md)|Easy|O(nlogn)|O(1)||
|No.LZOF_40|[最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)|[Solution](./LZOF_40/Solution.py)|[Note](./LZOF_40/note.md)|Easy|O(nlogk)|O(1)||
|No.LZOF_41|[连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)|[Solution](./LZOF_41/Solution.py)|[Note](./LZOF_41/note.md)|Easy|O(n)|O(1)||
|No.LZOF_49|[ 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)|[Solution](./LZOF_49/Solution.py)|[Note](./LZOF_49/note.md)|Medium|O(n)|O(1)||
|No.LZOF_48|[最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)|[Solution](./LZOF_48/Solution.py)|[Note](./LZOF_48/note.md)|Medium|O(n)|O(n)||
|No.LZOF_47|[礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)|[Solution](./LZOF_47/Solution.py)|[Note](./LZOF_47/note.md)|Medium|O(n)|O(n*2)||
|No.LZOF_46|[把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)|[Solution](./LZOF_46/Solution.py)|[Note](./LZOF_46/note.md)|Medium|O(n*2)|O(1)||
|No.LZOF_45|[把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)|[Solution](./LZOF_45/Solution.py)|[Note](./LZOF_45/note.md)|Medium|O(nlogn)|O(n)||
|No.LZOF_50|[第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)|[Solution](./LZOF_50/Solution.py)|[Note](./LZOF_50/note.md)|Easy|O(n)|O(n)||
|No.LZOF_52|[两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)|[Solution](./LZOF_52/Solution.py)|[Note](./LZOF_52/note.md)|Easy|O(n)|O(1)||
|No.LZOF_53_I|[在排序数组中查找数字I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)|[Solution](./LZOF_53_I/Solution.py)|[Note](./LZOF_53_I/note.md)|Easy|O(logn)|O(1)||
|No.LZOF_53_II|[0～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/)|[Solution](./LZOF_53_II/Solution.py)|[Note](./LZOF_53_II/note.md)|Easy|O(n)|O(1)||
|No.LZOF_54|[二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)|[Solution](./LZOF_54/Solution.py)|[Note](./LZOF_54/note.md)|Easy|O(nlogk)|O(n)||
|No.LZOF_55_I|[二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/)|[Solution](./LZOF_55_I/Solution.py)|[Note](./LZOF_55_I/note.md)|Easy|O(n)|O(1)||
|No.LZOF_55_II|[平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/)|[Solution](./LZOF_55_II/Solution.py)|[Note](./LZOF_55_II/note.md)|Easy|O(n)|O(1)||
|No.LZOF_56_I|[数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)|[Solution](./LZOF_56_I/Solution.py)|[Note](./LZOF_56_I/note.md)|medium|O(n)|O(1)||
|No.LZOF_57|[和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/)|[Solution](./LZOF_57/Solution.py)|[Note](./LZOF_57/note.md)|Easy|O(n)|O(1)||
|No.LZOF_57_II|[和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)|[Solution](./LZOF_57_II/Solution.py)|[Note](./LZOF_57_II/note.md)|Easy|O(n)|O(n)||
|No.LZOF_58_I|[翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/)|[Solution](./LZOF_58_I/Solution.py)|[Note](./LZOF_58_I/note.md)|Easy|O(n)|O(1)||
|No.LZOF_58_II|[左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)|[Solution](./LZOF_58_II/Solution.py)|[Note](./LZOF_58_II/note.md)|Easy|O(n)|O(1)||
|No.LZOF_59_I|[滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)|[Solution](./LZOF_59_I/Solution.py)|[Note](./LZOF_59_I/note.md)|Easy|O(n)|O(N)||
|No.LZOF_59_II|[队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)|[Solution](./LZOF_59_II/Solution.py)|[Note](./LZOF_59_II/note.md)|Medium|O(1)|O(N)||
|No.LZOF_68_I|[二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)|[Solution](./LZOF_68_I/Solution.py)|[Note](./LZOF_68_I/note.md)|Easy|O(n)|O(n)||
|No.LZOF_68_II|[二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)|[Solution](./LZOF_68_II/Solution.py)|[Note](./LZOF_68_II/note.md)|Medium|O(n)|O(n)||
|No.LZOF_67|[把字符串转换成整数](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/)|[Solution](./LZOF_67/Solution.py)|[Note](./LZOF_67/note.md)|Easy|O(n)|O(n)||
|No.LZOF_66|[构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)|[Solution](./LZOF_66/Solution.py)|[Note](./LZOF_66/note.md)|Easy|O(n)|O(n)||
|No.LZOF_65|[不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)|[Solution](./LZOF_65/Solution.py)|[Note](./LZOF_65/note.md)|Easy|O(n)|O(n)||
|No.LZOF_63|[股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)|[Solution](./LZOF_63/Solution.py)|[Note](./LZOF_63/note.md)|Medium|O(n)|O(1)||
|No.LZOF_65|[n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)|[Solution](./LZOF_65/Solution.py)|[Note](./LZOF_65/note.md)|Easy|O(n)|O(1)||
|No.LZOF_62|[圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)|[Solution](./LZOF_62/Solution.py)|[Note](./LZOF_62/note.md)|Easy|O(n)|O(n)||
|No.LZOF_61|[扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)|[Solution](./LZOF_61/Solution.py)|[Note](./LZOF_61/note.md)|Easy|O(n)|O(n)||
|No.LZOF_64|[求1+2+...+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)|[Solution](./LZOF_64/Solution.py)|[Note](./LZOF_64/note.md)|Medium|O(n)|O(n)||
|No.LZOF_56_II|[数组中数字出现的次数 II](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/)|[Solution](./LZOF_56_II/Solution.py)|[Note](./LZOF_56_II/note.md)|Medium|O(n)|O(1)||
|No.LZOF41|[数据流中的中位数](https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/)|[Solution](./LZOF41/Solution.py)|[Note](./LZOF41/note.md)|Hard|O(n^2)|O(n)||




## 程序员面试经典
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.CXY_01_01|[判定字符是否唯一](https://leetcode-cn.com/problems/is-unique-lcci/)|[Solution](./CXY_01_01/Solution.py)|[Note](./CXY_01_01/note.md)|Easy|O(n)|O(n)||
|No.CXY_01_02|[判定是否互为字符重排](https://leetcode-cn.com/problems/check-permutation-lcci/)|[Solution](./CXY_01_02/Solution.py)|[Note](./CXY_01_02/note.md)|Easy|O(n)|O(n)||
|No.CXY_01_03|[URL化](https://leetcode-cn.com/problems/string-to-url-lcci/)|[Solution](./CXY_01_03/Solution.py)|[Note](./CXY_01_03/note.md)|Easy|O(n)|O(1)||
|No.CXY_01_04|[回文排列](https://leetcode-cn.com/problems/palindrome-permutation-lcci/)|[Solution](./CXY_01_04/Solution.py)|[Note](./CXY_01_04/note.md)|Easy|O(n)|O(n)||
|No.CXY_01_05|[一次编辑](https://leetcode-cn.com/problems/one-away-lcci/)|[Solution](./CXY_01_05/Solution.py)|[Note](./CXY_01_05/note.md)|Medium|O(n)|O(1)||
|No.CXY_01_06|[字符串压缩](https://leetcode-cn.com/problems/compress-string-lcci/)|[Solution](./CXY_01_06/Solution.py)|[Note](./CXY_01_06/note.md)|Easy|O(n)|O(n)||
|No.CXY_01_07|[旋转矩阵](https://leetcode-cn.com/problems/rotate-matrix-lcci/)|[Solution](./CXY_01_07/Solution.py)|[Note](./CXY_01_07/note.md)|Medium|O(n)|O(1)||
|No.CXY_01_08|[零矩阵](https://leetcode-cn.com/problems/zero-matrix-lcci/)|[Solution](./CXY_01_08/Solution.py)|[Note](./CXY_01_08/note.md)|Medium|O(n^2)|O(1)||
|No.CXY_01_09|[字符串轮转](https://leetcode-cn.com/problems/string-rotation-lcci/)|[Solution](./CXY_01_09/Solution.py)|[Note](./CXY_01_09/note.md)|Easy|O(s1+s2)|O(n)||
|No.CXY_02_01|[移除重复节点](https://leetcode-cn.com/problems/remove-duplicate-node-lcci/)|[Solution](./CXY_02_01/Solution.py)|[Note](./CXY_02_01/note.md)|Easy|O(n)|O(n)||
|No.CXY_02_02|[返回倒数第 k 个节点](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/)|[Solution](./CXY_02_02/Solution.py)|[Note](./CXY_02_02/note.md)|Easy|O(n)|O(n)||
|No.CXY_02_03|[删除中间节点](https://leetcode-cn.com/problems/delete-middle-node-lcci/)|[Solution](./CXY_02_03/Solution.py)|[Note](./CXY_02_03/note.md)|Easy|O(1)|O(1)||
|No.CXY_02_04|[分割链表](https://leetcode-cn.com/problems/partition-list-lcci/)|[Solution](./CXY_02_04/Solution.py)|[Note](./CXY_02_04/note.md)|Medium|O(n)|O(1)||
|No.CXY_02_05|[链表求和](https://leetcode-cn.com/problems/sum-lists-lcci/)|[Solution](./CXY_02_05/Solution.py)|[Note](./CXY_02_05/note.md)|Medium|O(n)|O(n)||
|No.CXY_02_06|[回文链表](https://leetcode-cn.com/problems/palindrome-linked-list-lcci/)|[Solution](./CXY_02_06/Solution.py)|[Note](./CXY_02_06/note.md)|Medium|O(n)|O(1)||
|No.CXY_02_07|[链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/)|[Solution](./CXY_02_07/Solution.py)|[Note](./CXY_02_07/note.md)|Easy|O(n)|O(1)||
|No.CXY_02_08|[环路检测](https://leetcode-cn.com/problems/linked-list-cycle-lcci/)|[Solution](./CXY_02_08/Solution.py)|[Note](./CXY_02_08/note.md)|Easy|O(n)|O(1)||
|No.CXY_03_01|[三合一](https://leetcode-cn.com/problems/three-in-one-lcci/)|[Solution](./CXY_03_01/Solution.py)|[Note](./CXY_03_01/note.md)|Easy|O(n)|O(n)||
|No.CXY_03_02|[栈的最小值](https://leetcode-cn.com/problems/min-stack-lcci/)|[Solution](./CXY_03_02/Solution.py)|[Note](./CXY_03_02/note.md)|Easy|O(n)|O(1)||
|No.CXY_03_03|[堆盘子](https://leetcode-cn.com/problems/stack-of-plates-lcci/)|[Solution](./CXY_03_03/Solution.py)|[Note](./CXY_03_03/note.md)|Medium|O(n)|O(n)||
|No.CXY_03_04|[化栈为队](https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci/)|[Solution](./CXY_03_04/Solution.py)|[Note](./CXY_03_04/note.md)|Easy|O(n)|O(n)||
|No.CXY_03_05|[栈排序](https://leetcode-cn.com/problems/sort-of-stacks-lcci/)|[Solution](./CXY_03_05/Solution.py)|[Note](./CXY_03_05/note.md)|Medium|O(n)|O(n)||
|No.CXY_03_06|[动物收容所](https://leetcode-cn.com/problems/animal-shelter-lcci/)|[Solution](./CXY_03_06/Solution.py)|[Note](./CXY_03_06/note.md)|Easy|O(n)|O(n)||
|No.CXY_04_01|[节点间通路](https://leetcode-cn.com/problems/route-between-nodes-lcci/)|[Solution](./CXY_04_01/Solution.py)|[Note](./CXY_04_01/note.md)|Medium|O(n)|O(n)||
|No.CXY_04_02|[最小高度树](https://leetcode-cn.com/problems/minimum-height-tree-lcci/)|[Solution](./CXY_04_02/Solution.py)|[Note](./CXY_04_02/note.md)|Easy|O(n)|O(n)||
|No.CXY_04_03|[特定深度节点链表](https://leetcode-cn.com/problems/list-of-depth-lcci/)|[Solution](./CXY_04_03/Solution.py)|[Note](./CXY_04_03/note.md)|Medium|O(n)|O(n)||
|No.CXY_04_04|[检查平衡性](https://leetcode-cn.com/problems/check-balance-lcci/)|[Solution](./CXY_04_04/Solution.py)|[Note](./CXY_04_04/note.md)|Easy|O(n)|O(n)||
|No.CXY_04_05|[合法二叉搜索树](https://leetcode-cn.com/problems/legal-binary-search-tree-lcci/)|[Solution](./CXY_04_05/Solution.py)|[Note](./CXY_04_05/note.md)|Medium|O(n)|O(n)||
|No.CXY_04_06|[后继者](https://leetcode-cn.com/problems/successor-lcci/)|[Solution](./CXY_04_06/Solution.py)|[Note](./CXY_04_06/note.md)|Medium|O(n)|O(n)||
|No.CXY_04_08|[首个共同祖先](https://leetcode-cn.com/problems/first-common-ancestor-lcci/)|[Solution](./CXY_04_08/Solution.py)|[Note](./CXY_04_08/note.md)|Medium|O(n)|O(n)||
|No.CXY_04_10|[检查子树](https://leetcode-cn.com/problems/check-subtree-lcci/)|[Solution](./CXY_04_10/Solution.py)|[Note](./CXY_04_10/note.md)|Medium|O(n^2)|O(n)||
|No.CXY_04_12|[求和路径](https://leetcode-cn.com/problems/paths-with-sum-lcci/)|[Solution](./CXY_04_12/Solution.py)|[Note](./CXY_04_12/note.md)|Medium|O(n)|O(n)||
|No.CXY_08_01|[三步问题](https://leetcode-cn.com/problems/three-steps-problem-lcci/)|[Solution](./CXY_08_01/Solution.py)|[Note](./CXY_08_01/note.md)|Easy|O(n)|O(n)||
|No.CXY_08_02|[迷路的机器人](https://leetcode-cn.com/problems/robot-in-a-grid-lcci/)|[Solution](./CXY_08_02/Solution.py)|[Note](./CXY_08_02/note.md)|Medium|O(100^2)|O(n)||
|No.CXY_08_03|[魔术索引](https://leetcode-cn.com/problems/magic-index-lcci/)|[Solution](./CXY_08_03/Solution.py)|[Note](./CXY_08_03/note.md)|Easy|O(n)|O(1)||
|No.CXY_08_04|[幂集](https://leetcode-cn.com/problems/power-set-lcci/)|[Solution](./CXY_08_04/Solution.py)|[Note](./CXY_08_04/note.md)|Medium|O(n^2)|O(n)||
|No.CXY_08_05|[递归乘法](https://leetcode-cn.com/problems/recursive-mulitply-lcci/)|[Solution](./CXY_08_05/Solution.py)|[Note](./CXY_08_05/note.md)|Medium|O(n)|O(n)||
|No.CXY_08_06|[汉诺塔问题](https://leetcode-cn.com/problems/hanota-lcci/)|[Solution](./CXY_08_06/Solution.py)|[Note](./CXY_08_06/note.md)|Easy|O(2^n)|O(n)||

