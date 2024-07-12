class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n=len(s)
        def remove_ba(s):
            n,cnt=len(s),0
            stack=[]
            for i in range(n):
                if s[i]=='a':
                    if stack and stack[-1]=='b':
                        cnt+=1
                        stack.pop()
                    else:
                        stack.append(s[i])
                elif s[i]=='b':
                    stack.append(s[i])
                elif s[i]==',':
                    stack=[]
                else:
                    stack.append(',')
            return cnt,"".join(stack)
        def remove_ab(s):
            n,cnt=len(s),0
            stack=[]
            for i in range(n):
                if s[i]=='b':
                    if stack and stack[-1]=='a':
                        cnt+=1
                        stack.pop()
                    else:
                        stack.append(s[i])
                elif s[i]=='a':
                    stack.append(s[i])
                elif s[i]==',':
                    stack=[]
                else:
                    stack.append(',')
            return cnt,"".join(stack)
        if x>y:
            cnt_ab,st=remove_ab(s)
            cnt_ba,st=remove_ba(st)
            return cnt_ab*x+cnt_ba*y
        else:
            cnt_ba,st=remove_ba(s)
            cnt_ab,st=remove_ab(st)
            return cnt_ab*x+cnt_ba*y

''' Time Complexity--O(n)
    Space Complexity--O(n)'''
