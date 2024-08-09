class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(row,col):
            m,n=len(grid),len(grid[0])
            total=[[(0,0),(0,-1),(0,1)],[(0,0),(-1,0),(1,0)],[(-1,-1),(0,-1),(1,-1)],
            [(-1,1),(0,1),(1,1)],[(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)],
            [(-1,-1),(0,0),(1,1)],[(-1,1),(0,0),(1,-1)]]
            sm=-float('inf')
            st=set()
            for j in range(8):
                s,f=0,0
                for i in range(3):
                    nrow=row+total[j][i][0]
                    ncol=col+total[j][i][1]
                    if nrow>=0 and nrow<m and ncol>=0 and ncol<n and grid[nrow][ncol]>=1 and grid[nrow][ncol]<=9:
                        s+=grid[nrow][ncol]
                        st.add(grid[nrow][ncol])
                    else:
                        return False
                if sm==-float('inf'):
                    sm=s
                elif sm!=-float('inf') and sm!=s:
                    return False
            if len(st)==9:
                return True
            return False
        m,n=len(grid),len(grid[0])
        cnt=0
        for i in range(n):
            for j in range(n):
                if check(i,j):
                    cnt+=1
        return cnt
''' Time Complexity--O(m*n)
    Space Complexity--O(1)'''
