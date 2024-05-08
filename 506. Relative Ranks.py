class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap=[]
        n=len(score)
        for i in range(n):
            heapq.heappush(heap,[-score[i],i])
        placement_ranks=['Gold Medal','Silver Medal','Bronze Medal']
        cnt=0
        while heap:
            _,ind=heapq.heappop(heap)
            if cnt<3:
                score[ind]=placement_ranks[cnt]
            else:
                score[ind]=str(cnt+1)
            cnt+=1
        return score
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
