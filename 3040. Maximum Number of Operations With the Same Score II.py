class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def func(l,r,sm):
            if l==r or l>r:
                return 0
            x,y,z=0,0,0
            if nums[l]+nums[l+1]==sm:
                x=1+func(l+2,r,sm)
            if nums[l]+nums[r]==sm:
                y=1+func(l+1,r-1,sm)
            if nums[r]+nums[r-1]==sm:
                z=1+func(l,r-2,sm)
            return max(x,y,z)
        n=len(nums)
        return 1+max(func(2,n-1,nums[0]+nums[1]),func(1,n-2,nums[0]+nums[-1]),func(0,n-3,nums[-1]+nums[-2]))
''' Time Complexity--O(n^2)
    Space Complexity--O(n^2)'''
