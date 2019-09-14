## 思路

- 中序遍历二叉搜索树
- 二分查找 target 应该插入的结点 pos
- 比较 pos-1 和 pos 位置与 target 的差，返回差最小的那个
- time complexity O(n)


## 最优思路

- closest必然在查找路径上. 
- 因此迭代查询该路径，直到root为空。
- 在查询过程中，根据当前最小值保存 root.val

```Python
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min_ = float("inf")
        while root:
            tmp = abs(target - root.val)
            if tmp < min_:
                min_ = tmp
                result = root.val
                    
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                return root.val
        return result
```


