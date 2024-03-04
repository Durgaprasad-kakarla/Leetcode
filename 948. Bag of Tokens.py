class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n=len(tokens)
        l,r=0,n-1
        cnt=0
        maxi=0
        while l<=r:
            if power>=tokens[l]:
                cnt+=1
                maxi=max(maxi,cnt)
                power-=tokens[l]
                l+=1
            elif cnt>0:
                power+=tokens[r]
                cnt-=1
                r-=1
            else:
                break
        return maxi
''' Time Complexity--O(nlogn)
    Space Complexity--O(1)'''
