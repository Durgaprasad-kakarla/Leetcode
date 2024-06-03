class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n,m,l,r=len(s),len(t),0,0
        while l<n and r<m:
            if s[l]==t[r]:
                l+=1
                r+=1
            else:
                l+=1
        return m-r
''' Time Complexity--O(m+n)
    Space Complexity--O(1)'''
