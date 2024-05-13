class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            s1=''
            for j in range(m):
                s1+=str(grid[i][j])
            x=int(s1,2)
            s2=''
            for j in range(m):
                if grid[i][j]==1:
                    s2+='0'
                else:
                    s2+='1'
            y=int(s2,2)
            if x<y:
                for j in range(m):
                    if grid[i][j]==1:
                        grid[i][j]=0
                    else:
                        grid[i][j]=1
        for i in range(m):
            cnt_0,cnt_1=0,0
            for j in range(n):
                if grid[j][i]==0:
                    cnt_0+=1
                else:
                    cnt_1+=1
            if cnt_0>cnt_1:
                for j in range(n):
                    if grid[j][i]==1:
                        grid[j][i]=0
                    else:
                        grid[j][i]=1
        tot=0
        for i in range(n):
            s1=''
            for j in range(m):
                s1+=str(grid[i][j])
            x=int(s1,2)
            tot+=x
        return tot
''' Time Complexity--O(n*3m)
    Space Complexity--O(m)'''
