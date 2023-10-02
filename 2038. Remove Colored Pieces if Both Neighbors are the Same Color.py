class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnt,cnt_A=0,0
        n=len(colors)
        for i in range(n):
            if colors[i]=='A':
                cnt+=1
            else:
                if cnt>=3:
                    cnt_A+=(cnt-2)
                cnt=0
        if cnt>=3:
            cnt_A+=(cnt-2)
        cnt,cnt_B=0,0
        for i in range(n):
            if colors[i]=='B':
                cnt+=1
            else:
                if cnt>=3:
                    cnt_B+=(cnt-2)
                cnt=0
        if cnt>=3:
            cnt_B+=(cnt-2)
        if cnt_A>cnt_B:
            return True
        return False
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
