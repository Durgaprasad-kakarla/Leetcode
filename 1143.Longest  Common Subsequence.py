class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Using dynamic programming- top down approach
        m,n=len(text1),len(text2)
        c=[[None for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:#taking the first row and first column elements as zero
                    c[i][j]=0
                elif text1[i-1]==text2[j-1]:#if the characters are same in both the texts the add one to the previous row left diagonal element and put it in the c[i][j].
                    c[i][j]=1+c[i-1][j-1]
                else:#If the character are different in both the texts then put the max of the beside element and upper element of the current element in c[i][j].
                    c[i][j]=max(c[i][j-1],c[i-1][j])
        return c[m][n]#return the last element of the c
