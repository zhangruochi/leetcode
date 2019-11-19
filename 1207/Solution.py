from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr).values()
        return len(set(count)) == len(count)
        