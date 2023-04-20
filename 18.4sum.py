class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        if not nums:
            return res
        n=len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                target2=target-nums[j]-nums[i]
                front=j+1
                back=n-1
                while front<back:
                    twosum=nums[front]+nums[back]
                    if twosum<target2:
                        front+=1
                    elif twosum>target2:
                        back-=1
                    else:
                        res.append([nums[i],nums[j],nums[front],nums[back]])
                        while front<back and nums[front]==res[-1][2]:
                            front+=1
                        while front<back and nums[back]==res[-1][3]:
                            back-=1
                while j+1<n and nums[j+1]==nums[j]:
                    j+=1
            while i+1<n and nums[i+1]==nums[i]:
                i+=1
        return res
''' Time Complexity--O(n^3)
    Space Complexity--O(n)'''
