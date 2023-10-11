class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        maxi=0
        ind=-1
        n=len(maxHeights)
        maxsum=0
        for ind in range(n):
            heights=[0]*n
            heights[ind]=maxHeights[ind]
            if ind>0:
                for i in range(ind,0,-1):
                    if maxHeights[i-1]<heights[i]:
                        heights[i-1]=maxHeights[i-1]
                    else:
                        heights[i-1]=heights[i]
            if ind<n-1:
                for i in range(ind,n-1):
                    if maxHeights[i+1]>=heights[i]:
                        heights[i+1]=heights[i]
                    else:
                        heights[i+1]=maxHeights[i+1]
            maxsum=max(maxsum,sum(heights))
        return maxsum
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
