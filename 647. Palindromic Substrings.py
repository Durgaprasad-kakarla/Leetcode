class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        cnt=0
        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j]==s[i:j][::-1]:
                    cnt+=1
        return cnt
''' Time Complexity--O(n^2)
    Space Complexity-O(1)'''
