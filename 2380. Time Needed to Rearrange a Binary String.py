class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        x=s.count('1')
        cnt=0
        while s[:x].count('1')!=x:
            s=s.replace('01','10')
            cnt+=1
        return cnt
''' Time Complexity--O(n^2)
    Space Complexity--O(1)'''
