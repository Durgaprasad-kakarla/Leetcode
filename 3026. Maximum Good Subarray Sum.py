class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dic=defaultdict(lambda:inf)
        n=len(nums)
        pref=0
        maxi=-float('inf')
        for i,num in enumerate(nums):
            if dic[num]>pref:
                dic[num]=pref
            pref+=num
            maxi=max(maxi,pref-dic[num+k],pref-dic[num-k])
        return 0 if maxi==-float('inf') else maxi  
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
