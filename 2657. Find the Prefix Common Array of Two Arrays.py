class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dic={}
        n=len(A)
        lst=[]
        for i in range(n):
            if A[i] in dic:
                dic[A[i]]+=1
            else:
                dic[A[i]]=1
            if B[i] in dic:
                dic[B[i]]+=1
            else:
                dic[B[i]]=1
            cnt=0
            for i in dic:
                if dic[i]==2:
                    cnt+=1
            lst.append(cnt)
        return lst
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
