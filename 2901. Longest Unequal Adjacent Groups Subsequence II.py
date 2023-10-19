class Solution:
    def getWordsInLongestSubsequence(self, n: int, arr: List[str], groups: List[int]) -> List[str]:
        def hamming(str1,str2):
            if len(str1)!=len(str2):
                return False
            else:
                cnt=0
                n=len(str1)
                for i in range(n):
                    if str1[i]!=str2[i]:
                        cnt+=1
                if cnt==1:
                    return True
                return False
        dp=[1]*n
        hash=[1]*n
        for i in range(n):
            hash[i]=i
            for prev in range(i):
                if 1+dp[prev]>dp[i] and groups[i]!=groups[prev] and hamming(arr[prev],arr[i]):
                    dp[i]=1+dp[prev]
                    hash[i]=prev
        ans=-1
        lastindex=-1
        for i in range(n):
            if dp[i]>ans:
                ans=dp[i]
                lastindex=i
        temp=[]
        temp.append(arr[lastindex])
        while hash[lastindex]!=lastindex:
            lastindex=hash[lastindex]
            temp.append(arr[lastindex])
        return temp[::-1]
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
