class Solution:
    def minOperations(self, s: str) -> int:
        s1=''
        s2=''
        for i in range(len(s)):
            if i%2==0:
                s1+='0'
                s2+='1'
            else:
                s1+='1'
                s2+='0'
        cnt=0
        for i in range(len(s)):
            if s[i]!=s1[i]:
                cnt+=1
        mini=cnt
        cnt=0
        for i in range(len(s)):
            if s[i]!=s2[i]:
                cnt+=1
        return min(mini,cnt)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
