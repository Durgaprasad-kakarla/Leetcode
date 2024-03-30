class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n=len(possible)
        for i in range(n):
            if possible[i]==0:
                possible[i]=-1
        pref=[0]*n
        pref[0]=possible[0]
        sm=possible[0]
        for i in range(1,n):
            sm+=possible[i]
            pref[i]=sm
        print(pref)
        for i in range(n-1):
            x=pref[i]
            y=pref[n-1]-pref[i]
            if x>y:
                return i+1
        return -1
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
