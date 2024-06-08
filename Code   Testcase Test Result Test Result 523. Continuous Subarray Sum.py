class Solution:
    def checkSubarraySum(self, arr: List[int], k: int) -> bool:
        n=len(arr)
        sm=0
        dic={0:-1}
        for i in range(n):
            sm=(sm+arr[i])
            rem=(sm-k)%k
            if rem in dic and i-dic[rem]>1:
                return True
            if rem not in dic:
                dic[rem]=i
        return False
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
