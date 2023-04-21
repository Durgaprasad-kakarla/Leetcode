class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        list1=[]
        for i in image:
            list1.append(i[::-1])
        for i in range(len(list1)):
            for j in range(len(list1[0])):
                if list1[i][j]==0:
                    list1[i][j]=1
                else:
                    list1[i][j]=0
        return list1
 ''' Time Complexity--O(n^2)
     Space Complexity--O(n^2)'''
