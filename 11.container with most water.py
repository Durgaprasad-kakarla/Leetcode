class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max1=0
        while l<r:
            max1=max(max1,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r=r-1
        return max1
