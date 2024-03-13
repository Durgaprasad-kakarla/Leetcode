class Solution:
    def pivotInteger(self, n: int) -> int:
        pref=0
        sm=(n*(n+1))//2
        for i in range(1,n+1):
            pref+=i
            if pref==sm-pref+i:
                return i
        return -1
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
