class Solution:
    def minimumOperations(self, arr: List[int]) -> int:
        n=len(arr)
        next=[0 for i in range(n+1)]
        for ind in range(n-1,-1,-1):
            cur=[0 for i in range(n+1)]
            for prev in range(ind-1,-2,-1):
                l=next[prev+1]
                r=0
                if prev==-1 or arr[prev]<=arr[ind]:
                    r=1+next[ind+1]
                cur[prev+1]=max(l,r)
            next=cur
        return n-next[0]
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
