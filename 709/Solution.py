class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        diff = ord("a") - ord("A")
        for char in str:
            if char >= "A" and char <= "Z":
                res += chr(ord(char) + diff)
            else:
                res += char
        
        return res
        

class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for char in str:
            if char.isupper():
                res += char.lower()
            else:
                res += char
        
        return res


class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
        
        