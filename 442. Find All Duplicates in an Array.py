class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        lst=[]
        for i in dic:
            if dic[i]==2:
                lst.append(i)
        return lst
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
