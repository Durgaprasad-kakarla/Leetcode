class Solution:
    def countWays(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        cnt=0
        if nums[0]!=0:
            cnt+=1
        for i in range(n):
            if i==n-1:
                if nums[i]<(i+1):
                    cnt+=1
                return cnt
            else:
                if nums[i]<(i+1) and nums[i+1]>(i+1):
                    cnt+=1
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
