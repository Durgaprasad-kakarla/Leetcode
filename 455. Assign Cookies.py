class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r=0,0
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        cnt=0
        while l<n and r<m:
            if g[l]<=s[r]:
                cnt+=1
                l+=1
                r+=1
            else:
                r+=1
        return cnt
''' Time Complexity--O(nlogn)+O(mlogm)
    Space Complexity--O(1)'''
