class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        return (pow(5,n//2+n%2,mod)*pow(4,n//2,mod))%mod
''' Time Complexity--O(logn)
    Space Complexity--O(1)'''
