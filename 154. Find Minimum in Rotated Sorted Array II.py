class Solution:
    def findMin(self, arr: List[int]) -> int:
        n=len(arr)
        l,r=0,n-1
        mini=float('inf')
        while l<=r:
            mid=(l+r)//2
            print(l,r,mid)
            mini=min(mini,arr[mid])
            if arr[l]==arr[mid] and arr[mid]==arr[r]:
                l+=1
                r-=1
                continue
            if arr[mid]>arr[l]:
                if arr[mid]<=arr[r]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]>arr[r]:
                    l=mid+1
                else:
                    r=mid-1
        return mini
''' Time Complexity--O(logn)
    Space Complexity--O(1)'''
