class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        list1=[]
        nums.sort()
        for i,x in enumerate(queries):
            lsum,count1,j=0,0,0
            while j<len(nums) and lsum<=x:
                lsum=lsum+nums[j]
                if lsum<=x:#if lsum is less than or equal to the x then we can increment the count1 else we have to break.
                    count1=count1+1
                else:
                    break
                j+=1
            list1.append(count1)#append the count of the elements to the list1
        return list1
