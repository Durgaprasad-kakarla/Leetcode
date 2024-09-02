class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sm=sum(chalk)
        k=k%sm
        n=len(chalk)
        tot=0
        for i in range(n):
            if chalk[i]<=k:
                k-=chalk[i]
            else:
                return i 
        return -1
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
