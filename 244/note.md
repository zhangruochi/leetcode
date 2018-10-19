## 思路

- 用一个 HashMap 保存该单词所有出现的位置，key为单词，list里面保存所有的位置。**注意，此时list中的元素是有序的**

- 求两个有序数组里最小元素的差，可以用一下方法：
    
    - 最简单直接就是双重for循环，用一个变量保存最小的差，时间复杂度为O(n^2)
    
    - 对第二个列表中的所有元素在第一个列表里进行二分搜索. 时间复杂度为O(nlogn)
    ```Python
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
    ```
    - 第三种办法就是用两个指针同时标记两个数组，根据大小同时移动两个指针，时间复杂度为O(m+n)
    ```Python
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
    ```