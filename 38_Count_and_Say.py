#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        string = "1"

        for i in range(1, n):
            counter = 1
            flag = 1
            tmp_string = ""

            for char in string:
                if flag:
                    current_char = char
                    flag = 0
                    continue

                if char == current_char:
                    counter += 1

                # 字符串中间，遇到不同的字母则统建前一个字母的个数    
                else:
                    tmp_string += "{}{}".format(counter, current_char)
                    current_char = char
                    counter = 1
                    
            # 统计最后一个字母的个数        
            tmp_string += "{}{}".format(counter, current_char)        
            string = tmp_string


        return string

if __name__ == '__main__':
    solution = Solution() 
    print(solution.countAndSay(5))  
