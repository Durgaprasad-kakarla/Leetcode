class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        cnt=0
        tot=0
        sm=0
        for i in range(n-1):
            if colors[i]==colors[i+1]:
                if cnt==0:
                    sm+=neededTime[i]+neededTime[i+1]
                    maxi=max(neededTime[i],neededTime[i+1])
                else:
                    sm+=neededTime[i+1]
                    maxi=max(maxi,neededTime[i+1])
                cnt+=1
            else:
                if cnt>0:
                    tot+=(sm-maxi)
                    cnt=0
                    sm=0
        if cnt>0:
            tot+=(sm-maxi)
        return tot
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
