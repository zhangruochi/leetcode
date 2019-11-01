## 思路

如果player1 选择的位置为x，则player2选择的位置只能是x的left child, right child, parent. 因此，player2 能够占有的节点数目是以下三者的最大值：
1. x 的左子树的节点数目
2. x 的右子树的节点数目
3. 整棵树减去以x为root的子树之后的节点数目。
