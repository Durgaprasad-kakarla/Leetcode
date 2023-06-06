class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 or n==2:
            return 0
        d=nums[1]-nums[0]
        c=2
        total=0
        for i in range(1,n-1):
            if nums[i+1]-nums[i]==d:
                c+=1
            if nums[i+1]-nums[i]!=d and c<3:
                d=nums[i+1]-nums[i]
                c=2
            if (nums[i+1]-nums[i]!=d or i==n-2) and c>=3:
                x=c-2
                total+=(x*(x+1))//2
                c=2
                d=nums[i+1]-nums[i]
        return total
''' Time Complexity--O(n)
    Space Complexity--O(1)
