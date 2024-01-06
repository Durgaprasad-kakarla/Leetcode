class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr=[(startTime[i],endTime[i]) for i in range(len(startTime))]
        dic={}
        n=len(arr)
        for i in range(n):
            dic[arr[i]]=profit[i]
        arr=sorted(arr,key=lambda x:x[1])
        new_dic={}
        y=arr[0][1]
        for i in range(n):
            x=arr[i][0]
            while x not in new_dic and x>=y:
                x-=1
            if i>0:
                if x in new_dic:
                    new_dic[arr[i][1]]=max(new_dic[x]+dic[arr[i]],new_dic[arr[i-1][1]])
                else:
                    new_dic[arr[i][1]]=max(dic[arr[i]],new_dic[arr[i-1][1]])
            else:
                new_dic[arr[i][1]]=dic[arr[i]]
        return new_dic[arr[-1][1]]
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
