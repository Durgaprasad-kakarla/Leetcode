class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n=len(students)
        cnt_0,cnt_1=students.count(0),students.count(1)
        while (cnt_0>0 and cnt_1>0) or (cnt_0==0 and sandwiches and sandwiches[0]==1) or (cnt_1==0 and sandwiches and sandwiches[0]==0) :
            if students[0]==sandwiches[0]:
                x=students.pop(0)
                sandwiches.pop(0)
                if x==0:
                    cnt_0-=1
                else:
                    cnt_1-=1
            else:
                students.append(students.pop(0))
        return cnt_0+cnt_1
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
