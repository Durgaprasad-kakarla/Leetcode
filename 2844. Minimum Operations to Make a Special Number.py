class Solution:
    def minimumOperations(self, num: str) -> int:
        s=""
        n=len(num)
        for i in range(n-1,-1,-1):
            if '0' in s and (num[i]=='0' or num[i]=='5'):
                return n-i-2
            if '5' in s and (num[i]=='2' or num[i]=='7'):
                return n-i-2
            if  num[i]=='0':
                s+=num[i]
            if num[i]=='5':
                s+=num[i]
        if '0' in s:
            return n-1
        return n
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
