class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        x=0
        s=s.split(" ")
        for i in range(len(s)):
            if s[i].isnumeric():
                if x<int(s[i]):
                    x=int(s[i])
                else:
                    return False
        return True
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
