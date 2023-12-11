class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt=1
        n=len(arr)
        for i in range(1,n):
            if arr[i-1]==arr[i]:
                cnt+=1
            else:
                if cnt/n>0.25:
                    return arr[i-1]
                cnt=1
        if cnt/n>0.25:
            return arr[-1]
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
