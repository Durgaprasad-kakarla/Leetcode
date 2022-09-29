class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d=arr[1]-arr[0]
        for i in range(len(arr)-1,0,-1):
            if arr[i]-arr[i-1]!=d:
                return False
        return True
                
