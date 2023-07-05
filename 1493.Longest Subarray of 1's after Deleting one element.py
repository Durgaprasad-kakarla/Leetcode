class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_0,count_1=0,0
        start=0
        max_len=0
        n=len(nums)
        if sum(nums)==len(nums):
            return sum(nums)-1
        for i in range(n):
            while count_0>1:
                if nums[start]==1:
                    count_1-=1
                    start+=1
                else:
                    count_0-=1
                    start+=1
            if nums[i]==0:
                count_0+=1
            if nums[i]==1:
                count_1+=1
            if count_0==1:
                max_len=max(max_len,i-start)
        return max_len
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
