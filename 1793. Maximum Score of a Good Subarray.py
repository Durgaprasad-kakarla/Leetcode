class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def smaller(nums):
            n=len(nums)
            prev=[-1]*n
            stack=[]
            for i in range(n):
                while stack and nums[stack[-1]]>nums[i]:
                    stack.pop()
                if stack:
                    prev[i]=stack[-1]
                stack.append(i)
            next=[-1]*n
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]]>=nums[i]:
                    stack.pop()
                if stack:
                    next[i]=stack[-1]
                stack.append(i)
            return prev,next
        prev,next=smaller(nums)
        maxi=0
        n=len(nums)
        for i in range(n):
            if prev[i]==-1 and next[i]==-1:
                maxi=max(maxi,nums[i]*(n))
            elif prev[i]==-1 and next[i]!=-1 and next[i]>k:
                maxi=max(maxi,nums[i]*(next[i]))
            elif next[i]==-1 and prev[i]!=-1 and prev[i]<k:
                maxi=max(maxi,nums[i]*(n-1-prev[i]))
            elif prev[i]!=-1 and next[i]!=-1 and k>prev[i] and k<next[i]:
                maxi=max(maxi,nums[i]*(next[i]-prev[i]-1))
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
