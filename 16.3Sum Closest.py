class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        list1=[]
        nums.sort()
        closest=sys.maxsize
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while(l<r):
                threesum=nums[i]+nums[l]+nums[r]
                if closest>abs(threesum-target):
                        ele=threesum
                        closest=abs(threesum-target)
                if threesum>target:
                    r=r-1
                elif threesum<target:
                    l=l+1
                else:
                    while l<r and nums[l]==nums[l+1]:
                        l=l+1
                    while l<r and nums[r]==nums[r-1]:
                        r=r-1
                    l=l+1
                    r=r-1
        return ele
''' Time Complexity--O(n^2)
    Space Complexity--O(1)'''
