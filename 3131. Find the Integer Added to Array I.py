class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2)-min(nums1)
''' Time Complexity--O(n1+n2)
    Space Complexity--O(1)'''
