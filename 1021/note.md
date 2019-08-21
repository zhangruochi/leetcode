## 思路
- 首先要理解 primitive decomposition
> A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
- 其次要理解 primitive decomposition
> S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings. 
- 对S进行decomposition后，每部分的outermost parentheses出栈后**栈为空**，根据这个特点，只要把parentheses的位置入栈，当出栈后导致栈为空的元素即为outermost parentheses的左括号。