class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        n=len(mapping)
        dic={}
        for i in range(10):
            dic[i]=mapping[i]
        lst=[]
        for ind,ele in enumerate(nums):
            st=str(ele)
            s=''
            for i in range(len(st)):
                s+=str(dic[int(st[i])])
            lst.append([int(s),ind,ele])
        sorted_lst=[]
        for i in sorted(lst):
            sorted_lst.append(i[2])
        return sorted_lst
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''
