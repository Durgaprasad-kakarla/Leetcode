class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic=Counter(s)
        st=''
        for i in order:
            if i in dic:
                st+=(i*dic[i])
                del dic[i]
        for i in dic:
            st+=(i*dic[i])
        return st
''' Time Complexity--O(n1+n2)
    Space Complexity--O(n2)'''
