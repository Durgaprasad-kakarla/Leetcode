class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minutes=[]
        for d,s in zip(dist,speed):
            mins=math.ceil(d/s)
            minutes.append(mins)
        minutes.sort()
        n=len(minutes)
        cnt=0
        for i in range(n):
            if i<minutes[i]:
                cnt+=1
            else:
                return cnt
        return cnt
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
