class Solution:
    def removeVowels(self, S: str) -> str:
        res = ""
        vowels = set(["a","e","i","o","u"])
        for char in S:
            if char in vowels:
                continue
            res += char
        return res
        