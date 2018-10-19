"""
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""


class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words_dict = defaultdict(list)
        for index,word in enumerate(words):
            self.words_dict[word].append(index)
        

    def binary_search(self, array, key):
        low, high = 0, len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            
            if array[mid] < key:
                low = mid + 1
            elif array[mid] > key:
                high = mid - 1
            else:
                return mid

        return mid               

            
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_index = self.words_dict[word1]
        word2_index = self.words_dict[word2]

        min_distance = float("inf")
    
        for index in word2_index:
            search_result = self.binary_search(word1_index,index)
            candidates = [search_result-1, search_result, search_result+1]
            for candidate in candidates:
                if  candidate <= len(word1_index)-1 and candidate >= 0:
                    tmp_min = abs(word1_index[candidate] - index)
                    if tmp_min < min_distance:
                        min_distance = tmp_min

        return min_distance




class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words_dict = {}
        for index,word in enumerate(words):
            if word not in self.words_dict:
                self.words_dict[word] = [index]
            else:
                self.words_dict[word].append(index)
               
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_index = self.words_dict[word1]
        word2_index = self.words_dict[word2]

        min_d= float("inf")
    
        i1,i2 = 0,0

        while True:
            val1, val2 = word1_index[i1],word2_index[i2]
            min_d = min(min_d,abs(val1 - val2))

            if val1 > val2:
                i2 += 1
            else:
                i1 += 1

            if i1 >= len(word1_index) or i2 >= len(word2_index):
                break

        return min_d





























