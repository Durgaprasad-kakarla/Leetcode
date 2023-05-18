class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        list1=[]
        for i in edges:
            list1.append(i[1])
        list1=set(list1)
        list2=[]
        for i in range(n):
            if i not in list1:
                list2.append(i)
        return list2
''' Time Complexity--O(n+m)
    Space Compexity--O(n)'''
