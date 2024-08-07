class Solution:
    def numberToWords(self, num: int) -> str:
        numbers={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
        11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',
        18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',
        80:'Eighty',90:'Ninety'}
        if num==0:
            return 'Zero'
        num=str(num)
        n=len(num)
        lst=[]
        for i in range(n,0,-3):
            if i<3:
                lst.append(num[:i])
            else:
                lst.append(num[i-3:i])
        def func(s):
            if int(s)<=0:
                return ''
            st=''
            if len(s)>2 and s[0]!='0':
                st+=numbers[int(s[0])]+" "+'Hundred'+" "
            if len(s)>1:
                numb=int(s[-2:])
                if s[-2]=='1':
                    st+=numbers[numb]+" "
                else:
                    n=(numb//10)*10
                    rem=(numb%10)
                    if n!=0:
                        st+=numbers[n]+" "
                    if rem!=0:
                        st+=numbers[rem]+" "
            else:
                return numbers[int(s[0])]
            return st
        dic={0:'',1:'Thousand',2:'Million',3:'Billion'}
        for i in range(len(lst)):
            if func(lst[i])!='':
                lst[i]=func(lst[i])+" "+dic[i]+" "
            else:
                lst[i]=''
        s=''.join(lst[::-1])
        s=s.replace('  ',' ')
        return s.rstrip()
''' Time Complexity--O(len(n))
    Space Complexity--O(len(s))'''
