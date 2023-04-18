class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        s=''
        i,j=0,0
        while i<n or i<m:
            if i<n and i<m:
                s=s+word1[i]+word2[i]
                i+=1
            elif i>=n and i<m:
                s=s+word2[i]
                i+=1
            elif i>=m and i<n:
                s=s+word1[i]
                i+=1
        return s
''' Time Complexity--O(max(m,n))
    Space Complexity--O(m+n)'''
