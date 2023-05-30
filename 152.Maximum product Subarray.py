class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        prefprod,suffprod=1,1
        i,maxval,c1,c2=0,0,0,0
        while i<n:
            if nums[i]!=0:
                c1+=1
                prefprod*=nums[i]
            else:
                c1=0
                prefprod=1
            if nums[n-i-1]!=0:
                c2+=1
                suffprod*=nums[n-i-1]
            else:
                c2=0
                suffprod=1
            if c1>0:
                maxval=max(maxval,prefprod)
            if c2>0:
                maxval=max(maxval,suffprod)
            i+=1
        return max(nums) if maxval==0 else maxval
''' Time Complexity--O(n)
    Space Complexity--O(1)
