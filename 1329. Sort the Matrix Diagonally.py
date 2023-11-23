class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dic={}
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            for j in range(n):
                if i-j in dic:
                    dic[i-j].append(mat[i][j])
                else:
                    dic[i-j]=[mat[i][j]]
        for i in dic:
           dic[i]=sorted(dic[i])
        new_mat=[[-1 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i-j in dic:
                    new_mat[i][j]=dic[i-j].pop(0)
        return new_mat
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
