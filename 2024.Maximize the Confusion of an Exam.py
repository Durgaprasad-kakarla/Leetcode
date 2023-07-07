class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def func(answerKey,k):
            count_0,count_1,s,max_len=0,0,0,0
            n=len(answerKey)
            for i in range(n):
                while count_0>k:
                    if answerKey[s]=='T':
                        count_1-=1
                        s+=1
                    else:
                        count_0-=1
                        s+=1
                        break
                if answerKey[i]=='F':
                    count_0+=1
                if answerKey[i]=='T':
                    count_1+=1
                if count_0<=k:
                    max_len=max(max_len,i-s)
            return max_len
        n=len(answerKey)
        new=''
        for i in range(n):
            if answerKey[i]=='T':
                new+='F'
            else:
                new+='T'
        return max(func(answerKey,k),func(new,k))+1
''' Time Complexity--O(n)+O(n)
    Space Complexity--O(n)'''
