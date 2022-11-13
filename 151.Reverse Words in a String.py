class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        i=0
        #Firstly we splitted the string with seperator space
        while i<len(s):
            if s[i]=='':
                #remove the element in the s which has s[i]=''
                s.remove(s[i])
                #To avoid the index out of range error I decremented the i as we know that if we remove an element in an array then len will be reduced by 1
                i-=1
            i+=1
        s=s[::-1]
        st=" ".join(s)
        return st
