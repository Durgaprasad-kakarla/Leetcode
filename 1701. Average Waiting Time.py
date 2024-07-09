class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time,prev,n=0,-1,len(customers)
        for a,t in customers:
            tot=max(prev,a)+t
            waiting_time+=(tot-a)
            prev=tot
        return waiting_time/n
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
