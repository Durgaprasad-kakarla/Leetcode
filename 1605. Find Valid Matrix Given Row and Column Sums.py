class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n,m=len(rowSum),len(colSum)
        mat=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            flag=0
            for j in range(m):
                if rowSum[i]<=colSum[j]:
                    mat[i][j]=rowSum[i]
                    colSum[j]-=rowSum[i]
                    rowSum[i]=0
                    flag=1
                    break
            if flag==0:
                for j in range(m):
                    if rowSum[i]>=colSum[j]:
                        mat[i][j]=colSum[j]
                        rowSum[i]-=colSum[j]
                        colSum[j]=0
                    else:
                        mat[i][j]=rowSum[i]
                        colSum[j]-=rowSum[i]
                        rowSum[i]=0
        print(rowSum,colSum)
        return mat
''' Time Complexity--O(m*n)
    space Complexity--O(m*n)'''
