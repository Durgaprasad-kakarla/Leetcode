class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n=len(arr)
        dp={i:1 for i in arr}
        arr.sort()
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if arr[i]%arr[j]==0 and arr[i]//arr[j] in dp:
                    dp[arr[i]]+=dp[arr[j]]*dp[arr[i]//arr[j]]
        return sum(dp.values())%(10**9+7)
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
