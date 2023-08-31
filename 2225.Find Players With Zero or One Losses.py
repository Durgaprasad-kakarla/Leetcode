class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        st1=set()
        st2=set()
        dict1={}
        for i in matches:
            st1.add(i[0])
            st2.add(i[1])
            if i[1] in dict1:
                dict1[i[1]]+=1
            else:
                dict1[i[1]]=1
        lst2=[]
        for i in dict1:
            if dict1[i]==1:
                lst2.append(i)
        lst2.sort()
        lst1=list(st1-st2)
        lst1.sort()
        return [lst1,lst2]
''' Time Complexity--O(n+klogk)
    Space Complexity--O(n)'''
