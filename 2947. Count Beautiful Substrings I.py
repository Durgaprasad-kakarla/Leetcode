class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n=len(s)
        tot=0
        vowels=['a','e','i','o','u']
        for i in range(n):
            v,c=0,0
            if s[i] in vowels:
                v+=1
            else:
                c+=1
            for j in range(i+1,n):
                if s[j] in vowels:
                    v+=1
                else:
                    c+=1
                if v==c and (v*c)%k==0:
                    tot+=1
        return tot
''' Time Complexity--O(n^2)
    Space Complexity--O(1)'''
