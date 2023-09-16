class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=0
        if nums[0]>nums[-1]:
            for i in range(n-1,0,-1):
                if nums[i]<nums[i-1]:
                    cnt+=1
                    if cnt==1:
                        ele=n-i
            if cnt>1:
                return -1
            if cnt==1:
                return ele
        else:
            for i in range(1,n):
                if nums[i-1]>nums[i]:
                    return -1
            return 0
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
