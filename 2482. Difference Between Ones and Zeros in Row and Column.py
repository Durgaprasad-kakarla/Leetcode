class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        rez = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        list1=[]
        m1=len(grid[0])
        m2=len(grid)
        for i in grid:
            sum1=sum(i)
            list1.append([sum1,m1-sum1])
        for i in rez:
            sum1=sum(i)
            list1.append([sum1,m2-sum1])
        for i in range(m2):
            for j in range(m2,m1+m2):
                diff[i][j-m2]=list1[i][0]+list1[j][0]-list1[i][1]-list1[j][1]
        return diff
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
