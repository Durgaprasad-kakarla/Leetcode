class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        else:
            prefsum=[]
            total=0
            for i in range(n):
                total+=cardPoints[i]
                prefsum.append(total)
            maxi=0
            for i in range(k):
                total=prefsum[i]-prefsum[n-k+i]+prefsum[n-1]
                maxi=max(maxi,total)
            return max(maxi,prefsum[n-1]-prefsum[n-k-1])
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
