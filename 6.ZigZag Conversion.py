class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        res=''
        for r in range(numRows):
            x=2*(numRows-1)
            for i in range(r,len(s),x):
                res+=s[i]
                if r>0 and r<numRows-1 and i+x-2*r<len(s):
                    res+=s[i+x-2*r]
        return res
