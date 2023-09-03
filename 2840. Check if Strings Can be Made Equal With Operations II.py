class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_st1,even_st2,odd_st1,odd_st2='','','',''
        n=len(s1)
        for i in range(n):
            if i%2==0:
                even_st1+=s1[i]
                even_st2+=s2[i]
            else:
                odd_st1+=s1[i]
                odd_st2+=s2[i]
        return True if (sorted(even_st1)==sorted(even_st2) and sorted(odd_st1)==sorted(odd_st2)) else False 
''' Time Complexity--O(n) 
    Space Complexity--O(1)'''
