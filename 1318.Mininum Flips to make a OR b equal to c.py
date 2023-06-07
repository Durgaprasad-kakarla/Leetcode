class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def convert_to_binary(n):
            str1=''
            while n!=0:
                str1=str(n%2)+str1
                n=n//2
            return str1
        if a==b and b==c:
            return 0
        str1=convert_to_binary(a)
        str2=convert_to_binary(b)
        str3=convert_to_binary(c)
        n=max(len(str3),len(str2),len(str1))
        str1='0'*(n-len(str1))+str1
        str2='0'*(n-len(str2))+str2
        str3='0'*(n-len(str3))+str3
        count=0
        for i in range(n):
            if str3[i]=='0':
                if str1[i]=='0' and str2[i]=='0':
                    continue
                elif str1[i]=='1' and str2[i]=='1':
                    count+=2
                else:
                    count+=1
            else:
                if str1[i]=='0' and str2[i]=='0':
                    count+=1
        return count
''' Time Compelxity--O(max(len(str1),len(str2),len(str3))
    Space Complexity--O(max(len(str1),len(str2),len(str3))'''
