class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        st=[]
        dic={}
        for i in arr:
            x=bin(i).count('1')
            if x in dic:
                dic[x].append(i)
            else:
                dic[x]=[i]
        lst=[]
        for i in sorted(dic):
            for j in sorted(dic[i]):
                lst.append(j)
        return lst
''' Time Complexity--O(n*32)
    Space Complexity--O(n)'''
