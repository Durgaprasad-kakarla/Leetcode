class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum,rsum=0,sum(nums)-nums[0]
        if lsum==rsum:
            return 0
        for i in range(1,len(nums)):
            lsum=lsum+nums[i-1]#lsum is left sum before the index
            rsum=rsum-nums[i]#rsum is the right sum after index
            if lsum==rsum:#if they are equal return that index
                return i
        return -1
            
