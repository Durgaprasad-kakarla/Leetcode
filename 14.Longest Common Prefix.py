class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min=10000
        st=''
        for i in strs:
            if min>len(i):
                min=len(i)
                st=i
        #find the string which has minimum length in strs
        dict1={}#put the elements in the dictionary
        for i in range(len(st)):
            dict1[i]=st[i]
        str1=''
        for i in range(len(st)):
            count1,flag=0,0
            for s in strs:
                if s[i]==dict1[i]:#if s[i]==dict1[i] the increment count1 else break the loop
                    count1+=1
                else:
                    flag=1
                    break
            if flag==1:
                break
            if count1==len(strs):#if count1 is equal to the length of strs list
                str1=str1+dict1[i]
        return str1
