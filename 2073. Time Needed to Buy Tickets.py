class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ele=tickets[k]
        cnt=0
        n=len(tickets)
        for i in range(n):
            if tickets[i]>=ele:
                if i>k:
                    cnt+=ele-1
                else:
                    cnt+=ele
            else:
                cnt+=tickets[i]
        return cnt
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
