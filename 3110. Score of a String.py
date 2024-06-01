class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        n=len(s)
        for i in range(1,n):
            score+=abs(ord(s[i])-ord(s[i-1]))
        return score
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
