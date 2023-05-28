class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        list1=[]
        list2=[]
        if m*n==r*c:
            for i in range(m):
                for j in range(n):
                    list2.append(mat[i][j])
                    if len(list2)==c:
                        list1.append(list2)
                        list2=[]
            return list1
        else:
            return mat
''' Time Complexity--O(m*n)
    Space Complexity--O(r*c)
