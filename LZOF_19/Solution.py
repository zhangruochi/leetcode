"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s); m = len(p)

        # dp[m][n]
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # s = "", p = ""
        dp[0][0] = True

        # s != "", p = ""
        for _ in range(1,n+1):
            dp[0][_] = False

        # s = "", p != ""
        previous = 0
        for _ in range(1,m+1):
            if p[_-1] != "*":
                dp[_][0] = False
                previous += 1
            else:
                if previous == 1:
                    dp[_][0] = True
                    previous -= 1
                else:
                    dp[_][0] = False
        
        # p[j] == char
            # dp[i][j] = dp[i-1][j-1]
        # p[j] == "."
            # dp[i][j] = dp[i-1][j-1]
        # p[j] == "*"   
            # p[j-1] == s[i]
                # dp[i][j] = dp[i-1][j]
            #p[j-1] != s[i]
                # dp[i][j] = dp[i][j-2]


        for i in range(1,m+1):  # pattern  
            for j in range(1,n+1): # string
                if p[i-1].isalpha():
                    dp[i][j] = (p[i-1] == s[j-1]) and dp[i-1][j-1]
                elif p[i-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 不看
                    dp[i][j] = dp[i][j] or dp[i-2][j]
                    
                    # 看
                    if p[i-1 - 1] == s[j - 1] or p[i-1-1] == ".":
                        dp[i][j] = dp[i][j] or dp[i][j-1]
                
                        
        # print(dp)
        return dp[m][n]


                    

        

            


        