class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1,n2=len(str1),len(str2)
        l1,l2=0,0
        while l1<n1 and l2<n2:
            if (str1[l1]==str2[l2]) or (ord(str1[l1])+1==ord(str2[l2])) or (str1[l1]=='z' and str2[l2]=='a'):
                l1+=1
                l2+=1
            else:
                l1+=1
        if l2==n2:
            return True
        return False
''' Time Complexity--O(n1)
    Space Complexity--O(1)'''
