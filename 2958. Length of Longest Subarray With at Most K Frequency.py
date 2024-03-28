class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dic={}
        x=0
        n=len(nums)
        maxi=0
        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
            if dic[nums[i]]>k:
                while x<n and nums[x]!=nums[i]:
                    dic[nums[x]]-=1
                    x+=1
                dic[nums[x]]-=1
                x+=1
            maxi=max(maxi,i-x+1)
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
