class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)
        if k==1 or n==k:
            return 0
        new_list=[]
        for i in range(n-1):
            new_list.append(weights[i]+weights[i+1])
        new_list.sort()
        mini,maxi=0,0
        for i in range(k-1):
            mini+=new_list[i]
            maxi+=new_list[n-i-2]
        return maxi-mini
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
