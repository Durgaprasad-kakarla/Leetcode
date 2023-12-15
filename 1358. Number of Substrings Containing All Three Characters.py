class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def substringWithAtleastK(s,p):
            n=len(s)
            i,j,f=0,0,0
            cnt=0
            dic={}
            for i in range(n):
                while j<n and f<p:
                    if s[j] not in dic or dic[s[j]]==0:
                        f+=1
                        dic[s[j]]=1
                    else:
                        dic[s[j]]+=1
                    j+=1
                if f==p:
                    cnt+=(n-j+1)
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    f-=1
            return cnt
        return substringWithAtleastK(s,3)
''' Time Complexity--O(n)
    Space Complexity--O(3)'''
