class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        l1,r1,l2,r2=0,n1-1,0,n2-1
        while l1<=r1 and l2<=r2:
            if nums1[l1]==nums2[l2]:
                return nums1[l1]
            elif nums1[l1]>nums2[l2]:
                l2+=1
            else:
                l1+=1
        return -1
''' Time Complexity--O(n1+n2)
    Space Complexity--O(1)'''
