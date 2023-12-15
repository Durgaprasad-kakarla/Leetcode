class Solution:
    def totalFruit(self, s: List[int]) -> int:
        p=2
        i,j,f=0,0,0
        n=len(s)
        maxi=0
        dic={}
        for i in range(n):
            while j<n and f<=p:
                if s[j] not in dic or dic[s[j]]==0:
                    dic[s[j]]=1
                    f+=1
                else:
                    dic[s[j]]+=1
                if f<=p:
                    maxi=max(maxi,j-i+1)
                j+=1
            dic[s[i]]-=1
            if dic[s[i]]==0:
                f-=1
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(2)'''
