class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp=[1]*5
        cur=[1]*5
        for i in range(2,n+1):
            cur[0]=dp[1]+dp[4]+dp[2]
            cur[1]=dp[0]+dp[2]
            cur[2]=dp[1]+dp[3]
            cur[3]=dp[2]
            cur[4]=dp[2]+dp[3]
            dp=cur.copy()
        return sum(dp)%(10**9+7)
''' Time Complexity--O(n)
    Space Complexity--O(5)'''
