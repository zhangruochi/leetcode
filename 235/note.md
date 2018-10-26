##  思路

- 某两个元素p,q 的lowest common ancestor， 即为二叉搜索树中，值在这两个元素的值的中间的结点，且是唯一的。
- 因此可以递归求解，从根结点开始，如果此结点小于两个元素中的较小值，则递归右子树；
- 如果此结点大于两个元素中的较大值，递归左子树。
```Python
def lowestCommonAncestor(self, root, p, q):
        min_ = min([p.val,q.val])
        max_ = max([p.val,q.val])
        
        if root == p or root == q:
            return root
        if root.val > min_ and root.val < max_:
            return root
        elif root.val > max_:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < min_:
            return self.lowestCommonAncestor(root.right,p,q)
```