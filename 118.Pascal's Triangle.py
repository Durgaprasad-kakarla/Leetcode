from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list2=[]
        for i in range(numRows):
            list1=[]
            for j in range(i+1):
                list1.append(factorial(i)//(factorial(j)*factorial(i-j)))
            list2.append(list1)
        return list2
