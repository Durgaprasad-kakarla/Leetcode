class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        tot=0
        for i in range(n):
            if grumpy[i]==0:
                tot+=customers[i]
                customers[i]=0
        window=0
        print(customers,tot)
        for i in range(minutes):
            window+=customers[i]
        maxi=window
        for i in range(minutes,n):
            window+=customers[i]-customers[i-minutes]
            # print(window)
            maxi=max(maxi,window)
        return tot+maxi
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
