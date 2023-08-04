class Solution:
    def minPartitions(self, n: str) -> int:
        new_list=[]
        for i in n:
            new_list.append(int(i))
        return max(new_list)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
