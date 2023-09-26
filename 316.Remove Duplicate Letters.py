=len(s)
        stack=[]
        freq=dict(Counter(s))
        vis={i:False for i in set(s)}
        for i in s:
            if stack and stack[-1]>i and freq[stack[-1]]>0:
                if vis[i]==False:
                    while stack and stack[-1]>i and freq[stack[-1]]>0 and vis[i]==False:
                        vis[stack[-1]]=False
                        stack.pop(-1)
                else:
                    freq[i]-=1
            if not stack:
                stack.append(i)
                freq[i]-=1
                vis[i]=True
            elif stack[-1]>i:
                if freq[stack[-1]]==0:
                    if vis[i]==False:
                        stack.append(i)
                        vis[i]=True
                        freq[i]-=1
                    else:
                        freq[i]-=1
            else:
                if vis[i]==True:
                    freq[i]-=1
                else:
                    stack.append(i)
                    vis[i]=True
                    freq[i]-=1
        return "".join(stack)
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
