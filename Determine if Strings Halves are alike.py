class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        list1=['a','e','i','o','u']
        s1=s[:len(s)//2]
        s2=s[len(s)//2:]#taking half of the string in s1 ans s2
        count1,count2=0,0
        #count the vowels in both s1 and s2
        for i in range(len(s1)):
            if s1[i] in list1:
                count1+=1
            if s2[i] in list1:
                count2+=1
        if count1==count2:
            return True
        else:
            return False
