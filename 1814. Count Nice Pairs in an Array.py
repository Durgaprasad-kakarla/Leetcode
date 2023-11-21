class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)
        cnt=0
        for i in range(n):
            nums[i]=(nums[i]-int(str(nums[i])[::-1]))
        dic=Counter(nums)
        for i in dic:
            if dic[i]>1:
                cnt+=((dic[i]-1)*(dic[i]))//2
        return cnt%(10**9+7)
''' Time Complexity--O(n)  
    Space Complexity--O(n)'''
