class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @lru_cache(None)
        def dp(r,c):
            if c<0 or c>r:
                return 0
            if r==0 and c==0:
                return poured
            return max(dp(r-1,c-1)-1,0)/2+max(dp(r-1,c)-1,0)/2
        return min(1,dp(query_row,query_glass))
''' Time Complexity--O(query_row*query_glass)
    Space Complexity--O(query_row*query_glass)'''
