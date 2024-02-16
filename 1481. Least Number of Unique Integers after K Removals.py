class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic={}
        n=len(arr)
        for i in range(n):
            if arr[i] in dic:
                dic[arr[i]]+=1
            else:
                dic[arr[i]]=1
        new_dic={}
        for i in dic:
            if dic[i] in new_dic:
                new_dic[dic[i]]+=1
            else:
                new_dic[dic[i]]=1
        tot=0
        for i in sorted(new_dic.keys()):
            if k>=i*new_dic[i]:
                k-=i*new_dic[i]
                del new_dic[i]
            else:
                cnt=k//i
                tot+=new_dic[i]-cnt
                del new_dic[i]
                break
        return tot+sum(new_dic.values())
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
