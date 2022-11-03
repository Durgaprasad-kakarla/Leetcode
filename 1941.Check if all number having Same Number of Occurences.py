from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1=Counter(s)
        count1=s.count(s[0])
        for key,item in dict1.items():
            if item!=count1:
                return False
        return True
            
