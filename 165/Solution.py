"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
"""


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver_str1 = list(map(int,version1.split('.')))
        ver_str2 = list(map(int,version2.split('.')))
        
        for i in range(max(len(ver_str1),len(ver_str2))):
            if i >= len(ver_str1):
                val1 = 0
                val2 = ver_str2[i] 
            elif i >= len(ver_str2):
                val2 = 0
                val1 = ver_str1[i]
            else:
                val1 = ver_str1[i]
                val2 = ver_str2[i] 
            
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
            
        return 0

    def compareVersion2(self,version1,version2):
        from itertools import zip_longest  
        versions = (map(int,version.split('.')) for version in (version1,version2))
        for val1, val2 in zip_longest(*versions, fillvalue=0):
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
        return 0    
                    

if __name__ == '__main__':
    print(Solution().compareVersion2("01.1.1","1.1"))
