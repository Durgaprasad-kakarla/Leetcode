class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r=0,len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid+1]>arr[mid]:
                l=mid+1
            elif arr[mid-1]>arr[mid]:
                r=mid-1
 ''' Time Complexity--O(logn)
     Space Complexity--O(1)'''
