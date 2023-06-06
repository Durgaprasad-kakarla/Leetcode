class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def func(arr):
            arr.sort()
            d=arr[1]-arr[0]
            for i in range(len(arr)-1,0,-1):
                if arr[i]-arr[i-1]!=d:
                    return False
            return True
        list1=[]
        n=len(l)
        for i in range(n):
            list1.append(func(nums[l[i]:r[i]+1]))
        return list1
''' Time Complexity--O(n*len(l[i]:r[i]+1)log(len(l[i]:r[i]+1))
    Space Compexity--O(n)'''
