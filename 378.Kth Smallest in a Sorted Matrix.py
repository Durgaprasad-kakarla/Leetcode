class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        list2=[]
        for list1 in matrix:
            for i in list1:
                list2.append(i)
        heapq.heapify(list2)
        x=heapq.nsmallest(k,list2)
        return x[-1]
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
