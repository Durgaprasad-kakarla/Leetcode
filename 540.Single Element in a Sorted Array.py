class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        if len(nums)==1:
            return nums[0]
        while l<=r:
            mid=(l+r)//2
            if mid==l and mid==r:
                return nums[mid]
            elif nums[mid]==nums[mid-1]:
                if (mid-1-l)%2!=0:
                    r=mid-2
                elif r-l==2:
                    if nums[mid]==nums[mid+1]:
                        return nums[mid-1]
                    else:
                        return nums[mid+1]
                else:
                    l=mid+1
            elif nums[mid]==nums[mid+1]:
                if (mid-l)%2!=0:
                    r=mid-1
                elif r-l==2:
                    if nums[mid]==nums[mid+1]:
                        return nums[mid-1]
                    else:
                        return nums[mid+1]
                else:
                    l=mid+2
            else:
                return nums[mid]
        '''Time complexity:O(logn) and Space Complexity:O(1)'''
