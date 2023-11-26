class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                if j>0:
                    if matrix[j][i]==1:
                        matrix[j][i]=matrix[j-1][i]+1
                    else:
                        matrix[j][i]=0
        ans=0
        for i in range(m):
            matrix[i].sort(reverse=True)
            for j in range(n):
                ans=max(ans,(j+1)*matrix[i][j])
                print(matrix[i][j],ans)
        return ans          
        
''' Time Complexity--O(m*(n+logn))
    Space Complexity--O(1)'''
