class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq=sorted(list(Counter(word).values()))
        n=len(freq)
        def func(i,j,dp):
            if i==j:
                return 0
            if freq[j]-freq[i]<=k:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=min(freq[i]+func(i+1,j,dp),freq[j]-freq[i]-k+func(i,j-1,dp))
            return dp[i][j]
        dp=[[-1 for i in range(n)] for j in range(n)]
        return func(0,len(freq)-1,dp)
        
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
