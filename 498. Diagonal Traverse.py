class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i,j=0,0
        n=len(mat)
        m=len(mat[0])
        new_mat=[]
        for x in range(n):
            lst=[]
            while i>=0 and j<m and i<n and j>=0:
                lst.append(mat[i][j])
                i-=1
                j+=1
            i,j=x+1,0
            new_mat.append(lst)
        i=n-1
        j=1
        for x in range(1,m):
            lst=[]
            while i>=0 and i<n and j<m and j>=0:
                lst.append(mat[i][j])
                i-=1
                j+=1
            i=n-1
            j=x+1
            new_mat.append(lst)
        final=[]
        for i in range(len(new_mat)):
            if i%2==0:
                final+=new_mat[i]
            else:
                final+=new_mat[i][::-1]
        return final
''' Time Complexity--O(n*m)
    Space Complexity--O(n*m)'''
