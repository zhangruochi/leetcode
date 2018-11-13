"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""


import random 

class Codec:
    
    def __init__(self):
        self.table = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.table.append(longUrl)
        return "http://tinyurl.com/" + str(len(self.table)-1)
    
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.table[int(shortUrl.split("/")[-1])]
        

import random
class Codec:
    
    def __init__(self):
        self.long2short = {}
        self.short2long = {}
        self.dict = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long2short:
            return "http://tinyurl.com/" + self.long2short[longUrl]
        else:
            key = "".join([self.dict[random.randint(0,61)] for i in range(6)])
            while key in self.short2long:
                key = "".join([self.dict[random.randint(0,62)] for i in range(6)])
                
            self.short2long[key] = longUrl
            self.long2short[longUrl] = key
            return "http://tinyurl.com/" + key
        
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short2long[shortUrl.split("/")[-1]]
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))