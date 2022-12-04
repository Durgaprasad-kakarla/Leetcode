class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count1,lsum,rsum=0,0,sum(nums)
        #Taking leftsum of the array and comparing them.If leftsum is greater than or equal to the rightsum the increment the count and finally return the count
        for i in range(len(nums)-1):
            lsum=lsum+nums[i]
            rsum=rsum-nums[i]
            if lsum>=rsum:
                count1+=1
        return count1
