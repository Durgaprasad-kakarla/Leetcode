class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        new_list=[]
        i=1
        total=0
        while n>0:
            if k-i not in new_list:
                new_list.append(i)
                total+=i
                n-=1
            i+=1
        return total
''' Time Complexity--O(n)--approximately
    Space Complexity--O(n)'''
