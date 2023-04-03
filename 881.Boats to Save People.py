class Solution:
    def numRescueBoats(self, arr: List[int], limit: int) -> int:
        arr.sort()
        n=len(arr)
        l,r=0,n-1
        count=0
        while l<=r:
            if arr[l]+arr[r]<=limit:
                count+=1
                l+=1
                r-=1
            else:
                count+=1
                r-=1
        return count
'''Time Complexity--O(n)
   Space Complexity--O(1)'''
