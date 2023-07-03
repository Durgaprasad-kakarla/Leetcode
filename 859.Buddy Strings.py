class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        else:
            n=len(s)
            tot_count=0
            for i in range(n):
                if s[i]!=goal[i]:
                    tot_count+=1
                    if tot_count>2:
                        return False
                    if tot_count==1:
                        x=s[i]
                        a=goal[i]
                    if tot_count==2:
                        y=goal[i]
                        b=s[i]
            if tot_count==2:
                if x==y and a==b:
                    return True
                return False
            elif tot_count==0:
                if s==goal and len(s)!=len(set(s)):
                    return True
                return False
            return False
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
