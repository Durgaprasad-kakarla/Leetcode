class Solution:
    def largestGoodInteger(self, num: str) -> str:
        st=num[0]
        n=len(num)
        cnt=1
        maxi=""
        for i in range(1,n):
            if num[i]==num[i-1]:
                st+=num[i]
                cnt+=1
            else:
                st=num[i]
                cnt=1
            if cnt==3:
                if maxi<(st):
                    maxi=(st)
                st=""
        return maxi
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
