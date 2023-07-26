class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def func(mid,dist):
            sum=0
            n=len(dist)
            for i in range(len(dist)-1):
                sum+=math.ceil(dist[i]/mid)
            sum+=dist[n-1]/mid
            return sum
        l,r=1,10**7
        while l<=r:
            mid=(l+r)//2
            if func(mid,dist)<=hour:
                r=mid-1
            else:
                l=mid+1
        if l>10**7:
            return -1
        return l
''' Time Complexity--O(n*log(10**7))
    Space Complexity--O(1)'''
