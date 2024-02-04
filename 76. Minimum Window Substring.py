class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        dic_t,dic_s={},{}

        for i in t:
            if i in dic_t:
                dic_t[i]+=1
            else:
                dic_t[i]=1
        have,need=0,len(dic_t)
        res,res_len=[-1,-1],float('inf')

        l=0
        for i in range(len(s)):
            c=s[i]
            if c in dic_s:
                dic_s[c]+=1
            else:
                dic_s[c]=1
            if c in dic_t and dic_t[c]==dic_s[c]:
                have+=1
            while have==need:
                if (i-l+1)<res_len:
                    res=[l,i]
                    res_len=(i-l+1)
                dic_s[s[l]]-=1
                if s[l] in dic_t and dic_s[s[l]]<dic_t[s[l]]:
                    have-=1
                l+=1
        l,r=res
        if res_len!=float('inf'):
            return s[l:r+1]
        return ""
''' Time Complexity--O(len(s))
    Space Complexity--O(len(t))'''
