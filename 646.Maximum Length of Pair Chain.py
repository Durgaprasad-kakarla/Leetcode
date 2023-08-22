rr.sort()
        n=len(arr)
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        for ind in range(n-1,-1,-1):
            for prev in range(ind-1,-2,-1):
                l=dp[ind+1][prev+1]
                r=0
                if prev==-1 or arr[ind][0]>arr[prev][1]:
                    r=arr[ind][2]+dp[ind+1][ind+1]
                dp[ind][prev+1]=max(l,r)
        return dp[0][0]
''' Time Complexity--O(n^2)
    Space Complexity--O(n^2)'''
