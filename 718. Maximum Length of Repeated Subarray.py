class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m,n=len(nums1),len(nums2)
        prev=[0 for i in range(n+1)]
        maxi=0
        for i in range(1,m+1):
            cur=[0 for i in range(n+1)]
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    cur[j]=1+prev[j-1]
                    maxi=max(cur[j],maxi)
                else:
                    cur[j]=0
            prev=cur
        return maxi
''' Time Complexity--O(m*n)
    Space Complexity--O(n)'''
