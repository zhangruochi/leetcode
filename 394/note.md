##  思路

- 需要考虑两种字符串 3[a2[c]] 和 3[a]2[bc], 前一种嵌套，第二种平坦
- 观察上述两种情况，对于嵌套字符串：
    - 内部嵌套字符串求出来后要压栈，与前面字符串相加组成新的内部字符串
- 对于非嵌套字符串：
    - 解码第一段后需要保存，再解码第二段，然后将第二段的解码结果与前面的相加


- 因此，我们可以总结出，以上两种情况都是与前面字符串相加，所以我们用 stack.append([1,""]) 作为先导
- 在后续过程中，解码一部分后总是加到栈顶

```Python
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append([1,""])
        num = ""
        for char in s:
            if char.isdigit():
                num += char
            elif char == "[":
                stack.append([int(num),""])
                num = ""
            elif char == "]":
                k,str_ = stack.pop()
                stack[-1][1] += str_ * k
            else:
                stack[-1][1] += char

        return stack[-1][1]
```