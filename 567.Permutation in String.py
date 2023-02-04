class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        l=len(s1)
        l1=len(s2)
        if s1==list(s2):
            return True
        for i in range(l1//2):
            if sorted(s2[i:i+l])==s1:
                return True
            if sorted(s2[l1-l-i:l1-i])==s1:
                return True
        return False
