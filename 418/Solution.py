"""
Given arows x cols screen and a sentence represented as a list of strings, return the number oftimes the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

Example 1:

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
Example 2:

Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
Example 3:

Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.


Constraints:

1 <= sentence.length <= 100
1 <= sentence[i].length <= 10
sentence[i] consists of lowercase English letters.
1 <= rows, cols <= 2 * 104

"""

"""
# 超时
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        res = index = c = r = 0
        num_word = len(sentence)

        for word in sentence:
            if len(word) > cols:
                return 0

        while True:
            word = sentence[index % num_word]
            if r == 0 and c == 0:
                c = c + len(word)
            else:
                c =  1 + c + len(word)
            
            if c > cols:
                r += 1
                c = len(word)

                if r >= rows:
                    break 

            index += 1

            if index % num_word == 0:
                res += 1
        
        return res
"""

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        if len(sentence) == 0:
            return rows * cols


        word_len = [len(_) for _ in sentence]
        word_num = len(sentence)
        total_len = sum(word_len) + word_num

        idx = res = 0
        for i in range(rows):
            remain_cols = cols
            while remain_cols > 0:
                if word_len[idx] <= remain_cols:
                    remain_cols -= word_len[idx]
                    if remain_cols > 0:
                        remain_cols -= 1
                    idx += 1
                    if idx == word_num:
                       div, mod = divmod(remain_cols, total_len)
                       res += (div+1)
                       remain_cols = mod
                       idx = 0
                else:
                    break

        return res

            
            

        

        

        