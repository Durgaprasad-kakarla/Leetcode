class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l=min(bloomDay)
        r=max(bloomDay)
        if len(bloomDay)<m*k:
            return -1
        while l<=r:
            mid=(l+r)//2
            bouquets=0
            tot_count=0
            for i in bloomDay:
                if mid>=i:
                    tot_count+=1
                else:
                    bouquets+=tot_count//k
                    tot_count=0
            if tot_count!=0:
                bouquets+=tot_count//k
            if bouquets>=m:
                r=mid-1
            else:
                l=mid+1
        return l
''' Time Complexity--O(n*log(max(bloomDay)-min(bloomDay)))
    Space Complexity--O(1)'''
