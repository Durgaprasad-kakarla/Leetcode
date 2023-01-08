class Solution:
    def maxPoints(self, arr: List[List[int]]) -> int:
        dict1={}
        max1=0
        for i in range(len(arr)-max1-1):
            i_max=0
            for j in range(i+1,len(arr)):
                if arr[j][0]-arr[i][0]==0:#if x2-x1==0 then we have to put some value in the slope else we have to find the slope using the formula(y2-y1)/(x2-x1)
                    slope=100000001
                else:
                    slope=(float)(arr[j][1]-arr[i][1])/float(arr[j][0]-arr[i][0])
                if slope in dict1:#if slope is in dict1 then we have to increment the count of the value else give value 1 for that key
                    dict1[slope]=dict1[slope]+1
                else:
                    dict1[slope]=1
                i_max=i_max if i_max>dict1[slope] else dict1[slope]#if i_max is greater than dict1[slope] then put it in the max
            dict1.clear()#clearing the dict1 for every iteration of i
            max1=max1 if max1>i_max else i_max
        return max1+1
