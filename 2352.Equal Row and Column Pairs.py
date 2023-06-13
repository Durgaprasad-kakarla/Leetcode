class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        transpose=[[grid[j][i] for j in range(n)] for i in range(m)]
        count=0
        dict1={}
        for i in transpose:
            if str(i) in dict1:
                dict1[str(i)]+=1
            else:
                dict1[str(i)]=1
        for i in range(m):
            if str(grid[i]) in dict1:
                count+=dict1[str(grid[i])]
        return count
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
