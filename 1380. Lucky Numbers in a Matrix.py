class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        maximum=[]
        n,m=len(matrix),len(matrix[0])
        for i in range(m):
            maxi=0
            for j in range(n):
                maxi=max(maxi,matrix[j][i])
            maximum.append(maxi)
        lucky=[]
        for i in range(n):
            if min(matrix[i]) in maximum:
                lucky.append(min(matrix[i]))
        return lucky
''' Time Complexity--O(n*m)
    Space Complexity--O(m+n)'''
