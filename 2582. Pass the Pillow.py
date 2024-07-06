class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        mod=(2*n-2)
        if time%mod<n:
            return time%mod+1
        else:
            return (2*n-time%mod-1)%n
''' Time Complexity--O(1)
    Space Complexity--O(1)'''
