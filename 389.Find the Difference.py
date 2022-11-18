class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(len(t)):
            if t.count(t[i])!=s.count(t[i]):
                return t[i]
