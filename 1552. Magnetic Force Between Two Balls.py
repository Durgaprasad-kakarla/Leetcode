class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def func(position,m,x):
            cnt,n=1,len(position)
            prev=position[0]
            for i in range(1,n):
                if position[i]-prev>=x:
                    cnt+=1
                    prev=position[i]
            return cnt
        l,r=0,position[-1]-position[0]
        while l<=r:
            mid=(l+r)//2
            if func(position,m,mid)>=m:
                l=mid+1
            else:
                r=mid-1
        return r
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
