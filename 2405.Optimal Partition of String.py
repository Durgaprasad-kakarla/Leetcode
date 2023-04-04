class Solution:
    def partitionString(self, s: str) -> int:
        dict1={}
        count=0
        for i in s:
            if i in dict1.keys():
                dict1={}
                dict1[i]=1
                count+=1
            else:
                dict1[i]=1
        return count+1
'''Time Complexity--O(n*k)--here k is non repeated string length
   Space Complexity--O(n)'''
