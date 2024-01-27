class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        prev=[0]*(k+1)
        prev[0]=1
        for N in range(1,n+1):
            cur=[0]*(k+1)
            total=0
            for K in range(0,k+1):
                if K>=N:
                    total-=prev[K-N]
                total=(total+prev[K])%(10**9+7)
                cur[K]=total
            prev=cur
        return prev[k]
''' Time Complexity--O(n*k)
    Space Complexity--O(k)'''
