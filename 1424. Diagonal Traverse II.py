class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        dic={}
        for i in range(n):
            for j in range(len(nums[i])):
                if i+j in dic:
                    dic[i+j].append(nums[i][j])
                else:
                    dic[i+j]=[nums[i][j]]
        lst=[]
        for i in sorted(dic.keys()):
            lst+=dic[i][::-1]
        return lst
''' Time Complexity--O(n*m)
    Space Complexity--O(n+m)'''
