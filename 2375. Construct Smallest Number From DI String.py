class Solution:
    def smallestNumber(self, s: str) -> str:
        cnt=0
        if s[0]=='I':
            num=1
            x=1
        if s[0]=='D':
            cnt+=1
            num=0
            x=0
        n=len(s)
        for i in range(n):
            if s[i]=='I':
                if (i<n-1 and s[i+1]=='I') or (i==n-1):
                    num=num*10+(x+1)
                    x+=1
                    cnt=0
                if i<n-1 and s[i+1]=='D':
                    cnt+=1
            else:
                if (i<n-1 and s[i+1]=='D'):
                    cnt+=1
                if (i<n-1 and s[i+1]=='I') or i==n-1:
                    ele=cnt+x+1
                    x=cnt+x+1
                    for i in range(cnt+1):
                        num=num*10+ele
                        ele-=1
                    cnt=0
        return str(num)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
    
