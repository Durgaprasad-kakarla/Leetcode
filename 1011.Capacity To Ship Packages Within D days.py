class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        def func(mid,weights):
            days=1
            total=0
            for i in range(len(weights)):
                if total+weights[i]>mid:
                    days+=1
                    total=weights[i]
                else:
                    total+=weights[i]
            return days                            
        while l<=r:
            mid=(l+r)//2
            tot_days=func(mid,weights)
            if tot_days<=days:
                r=mid-1
            else:
                l=mid+1
        return l
''' Time Complexity--O(n*log(sum(weights)-max(weights)))
    Space Complexity--O(1)'''
