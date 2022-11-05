class Solution:
    def reverseVowels(self, s: str) -> str:
        list2=['a','e','o','u','i','A','E','I','O','U']
        i,j=0,len(s)-1
        s=list(s)
        while i<j:
            while i<j and s[i] not in list2:
                i+=1
            while i<j and s[j] not in list2:
                j-=1
            print(s[i],s[j])
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return "".join(s)
