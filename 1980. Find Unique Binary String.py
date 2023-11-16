class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length=len(nums[0])
        nums=[int(i,2) for i in nums]
        nums.sort()
        x=0
        for i in nums:
            if x!=i:
                y=bin(x)[2:]
                if len(y)!=length:
                    return (length-len(y))*"0"+y
                return y
            x+=1
        x=bin(x)[2:]
        x=(length-len(x))*"0"+x
        return x
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
