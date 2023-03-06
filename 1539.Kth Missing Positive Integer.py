class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(1,arr[-1]+1):
            if i not in arr:
                k-=1
                if k==0:
                    return i
        x=arr[-1]
        while k!=0:
            x=x+1
            k-=1
        return x
