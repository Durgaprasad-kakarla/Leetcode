class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dict1={}
        list2=set()
        if n==1 and trust==[]:
            return 1
        for i in trust:
            if i[1] not in dict1:
                dict1[i[1]]=[i[0]]
            else:
                dict1[i[1]].append(i[0])
            list2.add(i[0])
        for i in dict1.keys():
            if sum(dict1[i])==(n*(n+1))//2-i:
                if i not in list2:
                    return i
        return -1
                

        
