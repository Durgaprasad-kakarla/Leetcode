class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict1=Counter(arr)
        n=len(arr)
        tot,count=0,0
        for i in sorted(dict1.values(),reverse=True):
            tot+=i
            count+=1
            if tot>=n//2:
                return count
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
