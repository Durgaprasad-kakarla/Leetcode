class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def func(ind,temp,target,arr,list1):
            if ind==len(arr):
                if target==0 and len(temp)==k:
                    list1.append(temp)
                return 
            #pick
            if arr[ind]<=target:
                func(ind+1,temp+[arr[ind]],target-arr[ind],arr,list1)
            #not pick
            func(ind+1,temp,target,arr,list1)
        list1=[]
        temp=[]
        arr=[i for i in range(1,10)]
        func(0,temp,n,arr,list1)
        return list1
