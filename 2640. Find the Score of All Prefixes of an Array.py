class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        pref_max=[]
        maxi=0
        n=len(nums)
        for i in range(n):
            if maxi<nums[i]:
                maxi=nums[i]
            pref_max.append(maxi)
        pref_score=[0]*n
        pref_score[0]=nums[0]*2
        for i in range(1,n):
            pref_score[i]=pref_score[i-1]+nums[i]+pref_max[i]
        return pref_score
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
