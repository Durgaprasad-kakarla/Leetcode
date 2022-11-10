class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict1={}
        list1=[]
        for i in range(len(names)):
            dict1[heights[i]]=names[i]
        list2=sorted(dict1.keys())
        list2=list2[::-1]
        for i in list2:
            list2.append(dict1[i])
        return list2
