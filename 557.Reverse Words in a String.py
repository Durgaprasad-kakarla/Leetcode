class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split(' '))
        st=""
        for i in s:
            st=st+i[::-1]+' '
        return st[0:len(st)-1]
