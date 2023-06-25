class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n=len(locations)
        dp=[[0 for i in range(n)]for j in range(fuel+1)]
        dp[fuel][start]=1
        for f in range(fuel,-1,-1):
            for i in range(n):
                for j in range(n):
                    d=abs(locations[i]-locations[j])
                    if i!=j and f>=d:
                        dp[f-d][j]=(dp[f-d][j]+dp[f][i])
        total=0
        for i in range(fuel+1):
            total=total+dp[i][finish]
        return total%(10**9+7)
''' Time Complexity--O(fuel*n^2)
    Space Complexity--O(n*fuel)'''
