class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(x,y):
            if x+y>y+x:
                return -1
            else:
                return 1
        nums=[str(i) for i in nums]
        nums.sort(key=cmp_to_key(comp))
        st="".join(nums).lstrip('0')
        if st:
            return st
        return '0'
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
