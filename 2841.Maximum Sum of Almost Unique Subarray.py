class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        total=0
        n=len(nums)
        dictionary={}
        maxi=0
        for i in range(k):
            if nums[i] in dictionary:
                dictionary[nums[i]]+=1
            else:
                dictionary[nums[i]]=1
            total+=nums[i]
        if len(dictionary)>=m:
            maxi=max(maxi,total)
        for i in range(k,n):
            total+=(nums[i]-nums[i-k])
            dictionary[nums[i-k]]-=1
            if dictionary[nums[i-k]]==0:
                del dictionary[nums[i-k]]
            if nums[i] in dictionary:
                dictionary[nums[i]]+=1
            else:
                dictionary[nums[i]]=1
            if len(dictionary)>=m:
                maxi=max(maxi,total)
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
