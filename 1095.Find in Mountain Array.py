# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length=mountain_arr.length()
        print(length)
        l,r=1,length-2
        while l<=r:
            mid=(l+r)//2
            print(l,r,mid)
            left,ele,right=mountain_arr.get(mid-1),mountain_arr.get(mid),mountain_arr.get(mid+1)
            if left<ele<right:
                l=mid+1
            elif left>ele>right:
                r=mid-1
            else:
                break
        peak=mid
        print(mid)
        l,r=0,peak
        while l<=r:
            mid=(l+r)//2
            print(l,r,mid)
            val=mountain_arr.get(mid)
            if val>target:
                r=mid-1
            elif val<target:
                l=mid+1
            else:
                return mid
        l,r=peak,length-1
        print(length)
        while l<=r:
            mid=(l+r)//2
            print("dflj",l,r,mid)
            val=mountain_arr.get(mid)
            if val<target:
                r=mid-1
            elif val>target:
                l=mid+1
            else:
                return mid
        return -1
''' Time Complexity--O(logn)
    Space Complexity--O(1)'''
