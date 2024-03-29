class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt=0
        maxi=max(nums)
        s=0
        tot=0
        n=len(nums)
        for i in range(n):
            if nums[i]==maxi:
                cnt+=1
            if cnt==k:
                x=0
                while s<n and nums[s]!=maxi:
                    s+=1
                    x+=1
                s+=1
                cnt-=1
                tot+=(n-i)*(x+1)
        return tot
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
