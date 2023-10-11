class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start=sorted(a for a,b in flowers)
        print(start)
        end=sorted(b for a,b in flowers)
        lst=[]
        for p in people:
            lst.append(bisect_right(start,p)-bisect_left(end,p))
        return lst
''' Time Complexity--O(nlog(m)+mlogm)
    Space Complexity--O(n)'''
