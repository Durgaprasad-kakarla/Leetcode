class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n=len(arr)
        prefprod=[0]*n
        prod=1
        prefprod[0]=1
        for i in range(1,n):
            prod=arr[i-1]*prod
            prefprod[i]=prod
        prod=1
        for i in range(n-2,-1,-1):
            prod=arr[i+1]*prod
            prefprod[i]=prefprod[i]*prod
        return prefprod
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
