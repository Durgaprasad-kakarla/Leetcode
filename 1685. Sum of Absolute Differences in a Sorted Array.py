class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref=[0]*n
        prefsum=0
        for i in range(n):
            prefsum+=nums[i]
            pref[i]=prefsum
        lst=[]
        for i in range(n):
            cnt=0
            if i>0:
                cnt+=((nums[i]*i)-pref[i-1])
            if i<n-1:
                cnt+=(pref[n-1]-pref[i])-(nums[i]*(n-i-1))
            lst.append(cnt)
        return lst
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
