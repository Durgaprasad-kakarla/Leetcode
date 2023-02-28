class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def lcs(s1,s2):
            m,n=len(s1),len(s2)
            c=[[None for j in range(n+1)] for i in range(m+1)]
            for i in range(m+1):
                for j in range(n+1):
                    if i==0 or j==0:
                        c[i][j]=0
                    elif s1[i-1]==s2[j-1]:
                        c[i][j]=1+c[i-1][j-1]
                    else:
                        c[i][j]=max(c[i][j-1],c[i-1][j])
            return c[m][n]
        if len(s)==1:
            return 1
        return lcs(s,s[::-1])
