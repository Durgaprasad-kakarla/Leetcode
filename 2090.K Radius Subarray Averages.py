class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        prefsum=0
        pref=[0 for i in range(n)]
        for i in range(n):
            prefsum+=nums[i]
            pref[i]=prefsum
        res=[-1 for i in range(n)]
        if n<=2*k:
            return res
        else:
            for i in range(k,k+(n-2*k)):
                if i!=k:
                    res[i]=(pref[i+k]-pref[i-k-1])//(2*k+1)
                else:
                    res[i]=(pref[i+k])//(2*k+1)
            return res
''' Time Complexity--O(n) 
    Space Complexity--O(n)'''
