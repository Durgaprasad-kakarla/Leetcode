class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n=len(nums)
        new=[(nums[i]^k)-nums[i] for i in range(n)]
        new.sort(reverse=True)
        res=sum(nums)
        for i in range(0,n,2):
            if i==n-1:
                break
            path=new[i]+new[i+1]
            if path<=0:
                break
            res+=path
        return res
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
