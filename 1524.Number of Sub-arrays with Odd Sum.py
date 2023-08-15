class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pref=0
        n=len(arr)
        count,even_count,odd_count=0,0,0
        for i in range(n):
            pref+=arr[i]
            if pref%2==0:
                count+=odd_count
                even_count+=1
            else:
                count+=even_count+1
                odd_count+=1
        return count%(10**9+7)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
