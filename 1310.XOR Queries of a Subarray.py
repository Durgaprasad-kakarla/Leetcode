class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        m=len(queries)
        prefsum=[0]*n
        xor,prefsum[0]=arr[0],arr[0]
        list1=[]
        for i in range(1,n):
            xor=xor^arr[i]
            prefsum[i]=xor
        for i,query in enumerate(queries):
            if query[0]==0:
                list1.append(prefsum[query[1]])
            elif query[0]==query[1]:
                list1.append(arr[query[0]])
            else:
                l=query[0]
                r=query[1]
                xor=prefsum[r]^prefsum[l-1]
                list1.append(xor)
        return list1

''' Time Complexity--O(n)
    Space Complexity--O(n)'''
