"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""


class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dictionary = dictionary
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        elif len(word) == 1:
            return True 
        else:
            for cur in self.dictionary:
                if len(cur) < 2: continue
                if cur[0] == word[0] and cur[-1] == word[-1] and len(cur) == len(word) and cur != word:
                    return False
            return True    


class ValidWordAbbr:
        
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dictionary = {} 
        for word in dictionary:
            trans_word = self.transform(word)
            if trans_word not in self.dictionary:
                self.dictionary[trans_word] = word
            else:
                self.dictionary[trans_word] = False
    
    def transform(self,word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word)-2) + word[-1]
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        elif len(word) == 1:
            return True 
        else:
            key = self.transform(word)
            if key not in self.dictionary:
                return True
            else:
                return self.dictionary[key] == word    
        







