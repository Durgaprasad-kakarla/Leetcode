class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,cur,total):
            #if total is equal to the target then put it in the res list
            if total==target:
                res.append(cur.copy())
                return
            #If the length of the candidate<=i or total is greater than target the return the function
            if i>=len(candidates) or total>target:
                return
            #append an element in the list to check its sum is equal to the target 
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop()#remove the first element of the list
            dfs(i+1,cur,total)#checking the next index
        dfs(0,[],0)
        return res
