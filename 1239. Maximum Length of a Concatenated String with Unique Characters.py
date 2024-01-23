class Solution:
    def maxLength(self, arr: List[str]) -> int:
        new_arr=[]
        for i in arr:
            if len(set(i))==len(i):
                new_arr.append(i)
        global maxi
        maxi=0
        def func(ind,dic,arr):
            global maxi
            n=len(arr)
            if dic:
                maxi=max(maxi,len(dic))
            if ind==-1:
                return
            #not pick
            func(ind-1,dic,arr)
            flag=0
            for i in range(len(arr[ind])):
                if dic and arr[ind][i] in dic:
                    flag=1
                    break
            r=0
            if flag==0:
                if dic:
                    dic.update(dict(Counter(arr[ind])))
                    func(ind-1,dic,arr)
                    for i in arr[ind]:
                        del dic[i]
                else:
                    func(ind-1,dict(Counter(arr[ind])),arr)
            return 
        func(len(new_arr)-1,{},new_arr)
        return maxi
''' Time Complexity--O(2^n*len(s))
    Space Complexity--O(26)'''
