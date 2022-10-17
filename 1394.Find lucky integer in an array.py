class Solution:
    def findLucky(self, arr: List[int]) -> int:
        max1=0
        for i in list(set(arr)):
            if arr.count(i)==i and max1<arr.count(i):
                max1=arr.count(i)
        if max1==0:
            return -1
        else:
            return max1
