class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        dic={}
        for i in access_times:
            if i[0] in dic:
                dic[i[0]].append(i[1])
            else:
                dic[i[0]]=[i[1]]
        new=set()
        for j in dic:
            lst=sorted(dic[j])
            for i in range(len(lst)-2):
                if lst[i][:2]==lst[i+2][:2]:
                    new.add(j)
                elif int(lst[i][:2])+1==int(lst[i+2][:2]) and 60-int(lst[i][2:])+int(lst[i+2][2:])<60:
                    new.add(j)
        return new
