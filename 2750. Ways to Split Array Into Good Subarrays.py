class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        n=len(nums)
        count,total,i,flag=0,1,0,0
        while i<n:
            if nums[i]==1:
                flag=1
                break
            i+=1
        if flag==0:
            return 0
        while i<n:
            if nums[i]==0:
                count+=1
            else:
                if count==0:
                    i+=1
                    continue
                else:
                    total+=(total*count)
                    count=0
            i+=1
        return total%(10**9+7)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
