class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(ind1,ind2,str1,str2,dp):
            if ind1==0 or ind2==0:
                return 0
            if dp[ind1][ind2]!=0:
                return dp[ind1][ind2]
            if str1[ind1-1]==str2[ind2-1]:
                dp[ind1][ind2]=1+lcs(ind1-1,ind2-1,str1,str2,dp)
                return dp[ind1][ind2]
            dp[ind1][ind2]= max(lcs(ind1-1,ind2,str1,str2,dp),lcs(ind1,ind2-1,str1,str2,dp))
            return dp[ind1][ind2]
        dp=[[0 for i in range(len(str2)+1)]for j in range(len(str1)+1)]
        lcs(len(str1),len(str2),str1,str2,dp)
        i=len(str1)
        j=len(str2)
        s=''
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                s=s+str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                s=s+str1[i-1]
                i-=1
            else:
                s=s+str2[j-1]
                j-=1
        while i>0:
            s=s+str1[i-1]
            i-=1
        while j>0:
            s=s+str2[j-1]
            j-=1
        return s[::-1]
