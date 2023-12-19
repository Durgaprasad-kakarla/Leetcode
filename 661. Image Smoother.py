class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m=len(img)
        n=len(img[0])
        new_mat=[[0 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                rows=[-1,-1,-1,0,1,1,1,0]
                cols=[-1,0,1,1,1,0,-1,-1]
                sm=img[i][j]
                cnt=1
                for k in range(8):
                    row=i+rows[k]
                    col=j+cols[k]
                    if row>=0 and row<m and col>=0 and col<n:
                        sm+=img[row][col]
                        cnt+=1
                new_mat[i][j]=(sm)//cnt
        return new_mat

''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
