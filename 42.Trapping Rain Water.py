class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        prefsum=[]
        prefsum.append(arr[0])
        for i in range(1,n):
            prefsum.append(max(prefsum[-1],arr[i]))
        suffsum=[0]*n 
        suffsum[-1],max1=arr[-1],arr[-1]
        for i in range(n-2,-1,-1):
            max1=max(max1,arr[i])
            suffsum[i]=max1
        count=0
        for i in range(n):
            count=count+min(prefsum[i],suffsum[i])-arr[i]
        return count
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
