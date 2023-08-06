class Solution:
    def sortVowels(self, s: str) -> str:
        new_list=[]
        for i in s:
            if i=='a' or i=='e' or i=='o' or i=='i' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                new_list.append(i)
        new_list.sort()
        s_list=list(s)
        n=len(s)
        j=0
        for i in range(n):
            if s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='i' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                s_list[i]=new_list[j]
                j+=1
        return "".join(s_list)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
