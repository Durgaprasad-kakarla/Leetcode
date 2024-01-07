class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        dp=[defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]+=1+dp[j][diff]
                res+=1+dp[j][diff]
        return res-(n*(n-1))//2
''' Time Complexity--O(n*n)
    Space Complexity--O(n*n)'''
