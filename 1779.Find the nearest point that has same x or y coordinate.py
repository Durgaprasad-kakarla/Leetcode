class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min1=10000#we have take min1 as largest value
        count1=0
        index1=0
        for list1 in points:
            if list1[0]==x or list1[1]==y:#chech the point is valid or not
                if min1>abs(list1[0]-x)+abs(list1[1]-y):#check the manhattan distance is less than the min value
                    min1=abs(list1[0]-x)+abs(list1[1]-y)
                    index1=points.index(list1)#gives index of list1 in points
                count1=count1+1  
        if count1>0  :
            return index1
        else:#if it is not valid return -1
            return -1
