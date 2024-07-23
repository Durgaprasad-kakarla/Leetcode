class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        dic=dict(Counter(nums))
        final=[]
        for i,cnt in sorted(dic.items(),key=lambda x:x[1]):
            final+=[i]*cnt
        return final
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
