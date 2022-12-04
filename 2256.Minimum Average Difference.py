class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        lsum,rsum,index,n,min1=0,sum(nums),0,len(nums),1000000
        #Leftsum before i and rightsum after i 
        for i in range(n-1):
            lsum=lsum+nums[i]
            rsum=rsum-nums[i]
            #Finding the minimum of absolute difference between leftsum and rightsum from each i
            if min1>abs((lsum//(i+1))-(rsum//(n-i-1))):
                min1=abs((lsum//(i+1))-(rsum//(n-i-1)))
                index=i
        #Checking the last index and if average of total sum is less than min1 then return len(nums)-1
        if min1>sum(nums)//n:
            return n-1
        return index
