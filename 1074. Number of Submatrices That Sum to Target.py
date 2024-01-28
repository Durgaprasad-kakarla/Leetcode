class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        m,n=len(mat),len(mat[0])
        for row in mat:
            for i in range(n-1):
                row[i+1]+=row[i] 
        res = 0
        for i in range(n):
            for j in range(i, n):
                c = collections.defaultdict(int)
                cur, c[0] = 0, 1
                for k in range(m):
                    cur += mat[k][j] - (mat[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res
''' Time Complexity--O(m*n*n)
    Space Complexity--O(n)'''
