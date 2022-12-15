class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Using dynamic programming top down approach
        m,n=len(word1),len(word2)
        c=[[None for j in range(n+1)]for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:#Make the element of the first column and first row as '0'
                    c[i][j]=0
                elif word1[i-1]==word2[j-1]:#if characters of two characters are equal for two strings then add 1 to the left upper diagonal element in c[i][j]
                    c[i][j]=1+c[i-1][j-1]
                else:#If the characters of two characters are not equal then maximum element of upper and beside element in c[i][j]
                    c[i][j]=max(c[i-1][j],c[i][j-1])
        #Here we find the longest common subsequence c[m][n]
        return len(word1) + len(word2) - c[m][n] * 2#here we will get minimum steps required to make two strings equal.
