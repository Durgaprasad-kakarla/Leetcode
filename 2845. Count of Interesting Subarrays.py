class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n=len(nums)
        dic=defaultdict(int)
        dic[0]=1
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+(nums[i]%modulo==k)
        cnt=defaultdict(int)
        ans=0
        for i in range(n+1):
            j=prefix[i]-k
            ans+=cnt[j%modulo]
            cnt[prefix[i]%modulo]+=1
        return ans
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
