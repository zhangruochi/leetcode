class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        table = {char:index for index,char in enumerate(keyboard)}
        
        prev = keyboard[0]
        res = 0
        for char in word:
            res += abs(table[char] - table[prev])
            prev = char
        return res