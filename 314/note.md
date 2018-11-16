## 思路


Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]


- 根据观察，每一列是一个单独的 list, 每个 list 中的顺序按照层次由小到大的顺序
- 所以可以用一个 col 变量记录结点的col, 左子树的col值为父节点 col-1, 右子树的col值为父节点col+1
- 用 table 记录结果，key 为col, val 为 list, list中的值按层次遍历的顺序记录结点的val
- 最后按照key由小到大输出