class Solution:
    def minimizeStringValue(self, s: str) -> str:
        arr=[-1]*26
        n=len(s)
        s=list(s)
        lst=[]
        for i in range(n):
            if s[i]!='?':
                arr[ord(s[i])-97]+=1
        for i in range(n):
            if s[i]=='?':
                mini=float('inf')
                for j in range(26):
                    if mini>arr[j]:
                        mini=arr[j]
                        ele=chr(97+j)
                lst.append(ele)
                arr[ord(ele)-97]+=1
        lst.sort()
        for i in range(n):
            if s[i]=='?':
                s[i]=lst.pop(0)
        return "".join(s)
''' Time Complexity--O(n*26+nlogn)
    Space Complexity--O(26)'''
