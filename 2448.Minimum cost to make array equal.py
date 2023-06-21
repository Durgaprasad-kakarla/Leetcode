class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        maxcost=0
        n=len(nums)
        dict1={}
        sorted_nums=[]
        sorted_cost=[]
        for i in range(n):
            if  nums[i] not in dict1:
                dict1[nums[i]]=[cost[i]]
            else:
                dict1[nums[i]].append(cost[i])
        for i in sorted(dict1):
            for j in range(len(dict1[i])):
                sorted_nums.append(i)
            for i in dict1[i]:
                sorted_cost.append(i)
        prefsum=0
        pref=[]
        for i in sorted_cost:
            prefsum+=i
            pref.append(prefsum)
        x=prefsum/2
        for i in range(n):
            if pref[i]>x:
                index=i
                break
        ele=sorted_nums[index]
        total=0
        for i in range(n):
            total+=abs(sorted_nums[i]-ele)*sorted_cost[i]
        return total
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)
