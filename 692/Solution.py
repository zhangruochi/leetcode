from collections import Counter

class Comparable:
    def __init__(self,key,val):
        self.key = key
        self.val = val
    
    def __lt__(self, Other):
        if self.val < Other.val:
            return True
        elif self.val == Other.val:
            if self.key < Other.key:
                return False
            else:
                return True
        else:
            return False
        


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Elements with equal counts are ordered arbitrarily
        # return [p_[0] for p_ in Counter(words).most_common(k)]

        return [cp.key for cp in sorted([ Comparable(key,val) for key,val in Counter(words).items()], reverse = True)[:k]]