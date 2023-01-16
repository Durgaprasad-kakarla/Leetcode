class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        x=newInterval[0]#taking x,y to avoid overlapping in the intervals list
        y=newInterval[1]
        l=0
        new=[]
        for i in range(len(intervals)):
            if newInterval[0]  in range(intervals[i][0],intervals[i][1]+1):#if x lies in any list in intervals the l=l+1 and x is intervals[i][0] then break it
                l=i+1
                x=intervals[i][0]
                if newInterval[1]<intervals[i][1]:
                    y=intervals[i][1]
                break
            if x>intervals[i][0]:#If x is greater than the list's first element then append it to result list.
                new.append(intervals[i])
        for i in range(l,len(intervals)):#start from where we got the list in the intervals and find the y lies in the lists after previous list 
            if newInterval[1] in range(intervals[i][0],intervals[i][1]+1):#If y lies in any list in the intervals then y=intervals[i][0] and l=i+1
                l=i+1
                y=intervals[i][1]
                break
        new.append([x,y])#append the list which avoids overlapping.
        for j in range(l,len(intervals)):
            if intervals[j][0]>y:
                new.append(intervals[j])#append all other lists after we append the list and  avoid the overlapping.
        return new
