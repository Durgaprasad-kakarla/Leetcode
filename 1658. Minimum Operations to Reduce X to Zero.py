class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        dict1={}
        dict2={}
        n=len(nums)
        if sum(nums)<x:
            return -1
        pref=0
        for i in range(n):
            pref+=nums[i]
            dict1[pref]=i+1
        suff=0
        for i in range(n-1,-1,-1):
            suff+=nums[i]
            dict2[suff]=(n-i)
        mini=sys.maxsize
        if x in dict1:
            mini=min(dict1[x],mini)
        if x in dict2:
            mini=min(dict2[x],mini)
        for i in list(dict1.keys())[:n//2]:
            if x-i in dict2:
                mini=min(mini,dict1[i]+dict2[x-i])
        if mini==sys.maxsize:
            return -1
        return mini
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
