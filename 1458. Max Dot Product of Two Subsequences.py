class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        def func(i,j,dp,nums1,nums2):
            if i>=len(nums1) or j>=len(nums2):
                return sys.maxsize*-1
            if dp[i][j]!=sys.maxsize:
                return dp[i][j]
            l=nums1[i]*nums2[j]+func(i+1,j+1,dp,nums1,nums2)
            r=func(i+1,j,dp,nums1,nums2)
            t=func(i,j+1,dp,nums1,nums2)
            dp[i][j]=max(nums1[i]*nums2[j],l,r,t)
            return dp[i][j]
        dp=[[sys.maxsize for i in range(len(nums2))]for j in range(len(nums1))]
        return func(0,0,dp,nums1,nums2)
''' Time Complexity--O(n1*n2)
    Space Complexity--O(n1*n2)'''
