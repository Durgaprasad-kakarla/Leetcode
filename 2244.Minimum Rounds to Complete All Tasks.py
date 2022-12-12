class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dict1=Counter(tasks)
        count1=0
        for i in dict1.values():
            if i==1:#if i==1 then we cannot complete 2 or 3 tasks so return -1
                return -1
            if i==2:# if i==2 then increment the count by 1
                count1+=1
            elif i%3==0:#As we need to find the minimum rounds,if it is divisible by 3 then count that.
                count1+=(i//3)
            else:#If it is not divisible by 3 then count is i//3 and add 1 to it
                count1+=((i//3)+1)
        return count1
