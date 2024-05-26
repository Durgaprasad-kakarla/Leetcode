class Solution:
    def checkRecord(self, n: int) -> int:
        pre=[[0 for i in range(2)]for j in range(3)]
        for ind in range(n+1):
            curr=[[0 for i in range(2)]for j in range(3)]
            for prev in range(3):
                for a in range(2):
                    if ind==0:
                        curr[prev][a]=1
                        continue
                    l,r=0,0
                    if a==0:
                        l=pre[0][1]
                    if prev!=2:
                        r=pre[prev+1][a]
                    k=pre[0][a]
                    curr[prev][a]=(l+r+k)%(10**9+7)
            pre=curr
        return pre[0][0]%(10**9+7)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
        # def check(ind,prev,a):
        #     if ind<0:
        #         return 1
        #     if dp[ind][prev][a]!=-1:
        #         return dp[ind][prev][a]
        #     l,r,k=0,0,0
        #     if a==0:
        #         l=check(ind-1,0,1)
        #     r=0
        #     if prev!=2:
        #         r=check(ind-1,prev+1,a)
        #     k=check(ind-1,0,a)
        #     dp[ind][prev][a]=l+r+k
        #     return l+r+k
        # dp=[[[-1 for i in range(2)]for j in range(3)] for k in range(n)]
        # return check(n-1,0,0)%(10**9+7)
