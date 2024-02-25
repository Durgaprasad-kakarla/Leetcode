class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True         
        if 1 in nums: 
            return False        

        nums = sorted(set(nums), reverse = True)   
        if (n:=len(nums))==1 : 
            return True          

        for i in range(n-1):                       
            for j in range(i+1,n):
                if gcd(nums[i],nums[j])-1:          
                    nums[j]*= nums[i]             
                    break                       
            else: 
                return False                    
        return True 
''' Time Complexity--O(n^2)
    Space Complexity--O(1)'''
