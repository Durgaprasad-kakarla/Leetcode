class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size=0
        for i in s:
            if i.isnumeric():
                size*=int(i)
            else:
                size+=1
        n=len(s)
        for i in range(n-1,-1,-1):
            k=k%size
            if k==0 and s[i].isalpha():
                return s[i]
            elif s[i].isnumeric():
                size=size//int(s[i])
            else:
                size-=1
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
