class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0 for i in range(n)]for j in range(n)]
        left,right,top,bottom,x=0,n-1,0,n-1,1
        while left<=right and top<=bottom:
            for i in range(left,right+1,1):
                mat[top][i]=x
                x+=1
            top+=1
            for i in range(top,bottom+1,1):
                print(i,right)
                mat[i][right]=x
                x+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    mat[bottom][i]=x
                    x+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    mat[i][left]=x
                    x+=1
                left+=1
        return mat
''' Time Complexity--O(n*n)
    Space Complexity--O(n*n)'''
