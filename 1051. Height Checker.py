class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n=len(heights)
        expected=sorted(heights)
        cnt=0
        for i in range(n):
            if expected[i]!=heights[i]:
                cnt+=1
        return cnt
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
