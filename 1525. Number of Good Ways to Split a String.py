class Solution:
    def numSplits(self, s: str) -> int:
        st=set()
        n=len(s)
        pref,suff=[0]*n,[0]*n
        pref[0],suff[n-1]=1,1
        st.add(s[0])
        for i in range(1,n):
            if s[i] not in st:
                st.add(s[i])
                pref[i]+=pref[i-1]+1
            else:
                pref[i]=pref[i-1]
        st=set()
        st.add(s[n-1])
        for i in range(n-2,-1,-1):
            if s[i] not in st:
                st.add(s[i])
                suff[i]+=suff[i+1]+1
            else:
                suff[i]=suff[i+1]
        cnt=0
        for i in range(n-1):
            if pref[i]==suff[i+1]:
                cnt+=1
        return cnt
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
