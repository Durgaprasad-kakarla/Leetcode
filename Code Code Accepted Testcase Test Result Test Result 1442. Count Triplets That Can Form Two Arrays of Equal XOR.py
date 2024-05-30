class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n,cnt=len(arr),0
        for i in range(n):
            xor=arr[i]
            for j in range(i+1,n):
                xor^=arr[j]
                if xor==0:
                    print(j-i)
                    cnt+=(j-i)
        return cnt
''' Time Complexity--O(n^2)
    Space Complexity--O(1)'''
