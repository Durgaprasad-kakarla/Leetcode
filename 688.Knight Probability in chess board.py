class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        current = [[0 for i in range(n)] for j in range(n)]
        next1 = [[0 for i in range(n)] for j in range(n)]
        current[row][column] = 1
        all_pos = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(2,-1),(1,-2)]
        for l in range(k):
            for i in range(n): 
                for j in range(n):
                    if current[i][j] != 0:
                        for pos in all_pos: 
                            temp_x = i + pos[0]
                            temp_y = j + pos[1]
                            if 0 <= temp_x < n and 0 <= temp_y < n:
                                next1[temp_x][temp_y] += (current[i][j] / 8) 
            current, next1 = next1, [[0 for i in range(n)] for j in range(n)] 
        total_sum = 0
        for item in current:
            total_sum += sum(item)
        return total_sum
''' Time Complexity--O(n*n*k*8)
    Space Complexity--O(n*n)'''
