class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n=len(books)
        dp=[float('inf') for i in range(n+1)]
        dp[0]=0
        for i in range(1,n+1):
            j=i-1
            Width=shelfWidth
            max_height=0
            while j>=0 and Width>=books[j][0]:
                Width-=books[j][0]
                max_height=max(max_height,books[j][1])
                dp[i]=min(dp[i],dp[j]+max_height)
                j-=1
        return dp[n]
''' Time Complexity--O(n^2)
    Space Complexity--O(n)'''
