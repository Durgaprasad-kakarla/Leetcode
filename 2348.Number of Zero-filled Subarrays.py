class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count1=0
        x=0
        for i in range(len(nums)):
            if nums[i]==0:
                count1+=1
            elif nums[i]!=0 and nums[i-1]==0:
                x+=(count1*(count1+1))//2
                count1=0
        if count1!=0:
            return x+((count1*(count1+1))//2)
        else:
            return x
