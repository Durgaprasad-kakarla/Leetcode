class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic={}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]].append(i)
            else:
                dic[s[i]]=[i]
        tot=0
        for i in dic:
            if len(dic[i])>1:
                lst=dic[i]
                cnt=0
                st=set()
                for j in range(lst[0]+1,lst[-1]):
                    st.add(s[j])
                tot+=len(st)
        return tot
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
