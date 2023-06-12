class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums==[]:
            return []
        start=nums[0]
        count=1
        ranges=[]
        n=len(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
            else:
                if count==1:
                    ranges.append(str(nums[i-1]))
                else:
                    str1=str(start)+"->"+str(nums[i-1])
                    ranges.append(str1)
                start=nums[i]
                count=1
        if count==1:
            ranges.append(str(nums[n-1]))
        else:
            str1=str(start)+"->"+str(nums[n-1])
            ranges.append(str1)
        return ranges
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
