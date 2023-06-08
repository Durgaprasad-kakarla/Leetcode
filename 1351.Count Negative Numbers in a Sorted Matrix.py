class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        count=0
        for i in range(n):
            l,r=0,m-1
            x=r
            while l<=r:
                mid=(l+r)//2
                if grid[i][mid]<0 and mid!=0 and grid[i][mid-1]<0:
                    r=mid-1
                elif grid[i][mid]>=0:
                    l=(mid+1)
                else:
                    count+=(x-mid)+1
                    break
        return count
 ''' Time Complexity--O(nlogm)
     Space Complexity--O(1)
