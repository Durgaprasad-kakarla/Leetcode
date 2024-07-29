class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        lesser,greater=defaultdict(int),defaultdict(int)
        for i in range(n):
            for j in range(i+1,n):
                if rating[i]>rating[j]:
                    lesser[i]+=1
                else:
                    greater[i]+=1
        tot=0
        for i in range(n):
            for j in range(i+1,n):
                if rating[i]<rating[j]:
                    tot+=greater[j]
                else:
                    tot+=lesser[j]
        return tot
''' Time Complexity--O(n^2)
    Space Complexity--O(n^2)'''
