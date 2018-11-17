"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

class Solution:

    def operation(self,s):
        stack = []
        for char in s:
            if char == "#":
                if len(stack) == 0:
                    pass
                else:
                    stack.pop()
            else:
                stack.append(char)
        return stack        


    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_s = self.operation(S)
        stack_t = self.operation(T)

        return stack_s == stack_t

    def findNext(self,string):
        skip = 0
        for i in reversed(range(len(string))):
            if string[i] == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield string[i]

    def backspaceCompare2(self,S,T):
        import itertools
        return all(x == y for x, y in
                   itertools.zip_longest(self.findNext(S), self.findNext(T)))

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(s):
            stack = []
            for char in s:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
                    
            return "".join(stack)
        return build(S) == build(T)
            


if __name__ == '__main__':
    print(Solution().backspaceCompare(S = "a##c", T = "#a#c"))
    print(Solution().backspaceCompare2(S = "a##c", T = "#a#c"))          












