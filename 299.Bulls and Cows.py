class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dict1=Counter(secret)
        dict2=Counter(guess)
        n=len(secret)
        b,c=0,0
        for i in range(n):
            if secret[i]==guess[i]:
                b+=1
        for i in dict1:
            if dict2[i]:
                c+=min(dict1[i],dict2[i])
        return str(b)+"A"+str(c-b)+"B"
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
