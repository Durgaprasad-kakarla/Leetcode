class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        n=len(arr)
        arr.sort()
        hash=[i for i in range(n)]
        dp=[1]*n
        lastindex=0
        maxi=0
        for i in range(n):
            hash[i]=i
            for prev in range(i):
                if arr[i]%arr[prev]==0 and 1+dp[prev]>dp[i]:
                    dp[i]=1+dp[prev]
                    hash[i]=prev
            if dp[i]>maxi:
                maxi=dp[i]
                lastindex=i
        temp=[]
        temp.append(arr[lastindex])
        while hash[lastindex]!=lastindex:
            lastindex=hash[lastindex]
            temp.append(arr[lastindex])
        return temp
