class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        m=len(score)
        dict1={}
        list2=[]
        for list1 in score:
            dict1[list1[k]]=list1
        for i in sorted(dict1.keys(),reverse=True):
            list2.append(dict1[i])
        return list2
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
