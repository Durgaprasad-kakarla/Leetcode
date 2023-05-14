class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        dict1={}
        for i in boxTypes:
            if i[1] in dict1:
                dict1[i[1]]+=i[0]
            else:
                dict1[i[1]]=i[0]
        max1=0
        for i in sorted(dict1.keys(),reverse=True):
            if dict1[i]<truckSize:
                max1+=dict1[i]*i
            else:
                max1+=(truckSize)*i
                break
            truckSize=truckSize-dict1[i]
        return max1
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
