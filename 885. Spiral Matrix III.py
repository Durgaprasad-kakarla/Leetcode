class Solution:
    def spiralMatrixIII(self, m: int, n: int, row: int, col: int) -> List[List[int]]:
        positions=[[row,col]]
        steps=1
        i,j=row,col
        def check(i,j):
            if i>=0 and j>=0 and i<m and j<n:
                return True
            return False
        while len(positions)<m*n:
            #Go Right
            for _ in range(steps):
                i,j=i,j+1
                if check(i,j):
                    positions.append([i,j])
            #Go Down
            for _ in range(steps):
                i,j=i+1,j
                if check(i,j):
                    positions.append([i,j])
            steps+=1
            #Go Left
            for _ in range(steps):
                i,j=i,j-1
                if check(i,j):
                    positions.append([i,j])
            #Go Up
            for _ in range(steps):
                i,j=i-1,j
                if check(i,j):
                    positions.append([i,j])
            steps+=1
        return positions
''' Time Complexity--O(m*n)
    Space Complexity--O(m*n)'''
