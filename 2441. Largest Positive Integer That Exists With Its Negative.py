class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        dic1={}
        dic2={}
        maxi=-1
        for i in nums:
            if i not in dic1:
                dic1[i]=1
            if i not in dic2:
                dic2[i]=1
            if i in dic1 and -1*i in dic2:
                maxi=max(maxi,abs(i))
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
