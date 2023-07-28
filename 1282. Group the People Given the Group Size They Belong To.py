class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        new_dict={}
        n=len(groupSizes)
        for i in range(n):
            if groupSizes[i] in new_dict:
                new_dict[groupSizes[i]].append(i)
            else:
                new_dict[groupSizes[i]]=[i]
        newlist=[]
        for i in new_dict:
            n=len(new_dict[i])
            for j in range(0,n,i):
                newlist.append(new_dict[i][j:j+i])
        return newlist
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
