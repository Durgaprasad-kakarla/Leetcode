class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n,cnt=len(arr),0
        for i in range(n):
            if arr[i]&1==1:
                cnt+=1
            else:
                if cnt>2:
                    return True
                cnt=0
        if cnt>2:
            return True
        return False
''' Time Complexity--O(n)
    space Complexity--O(1)'''
