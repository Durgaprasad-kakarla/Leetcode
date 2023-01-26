import itertools
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        st=''
        for i in range(1,n+1):
            st=st+str(i)
        list2=list(itertools.permutations(st,n))#It gives all permutations of that string
        return "".join(list2[k-1])#k the element will be printed from list2


 
