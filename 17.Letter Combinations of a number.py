class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digitsToChar={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def backtrack(i,curstr):
            if len(curstr)==len(digits):##if this condition is true then then we have to append the res with curstr
                res.append(curstr)
                return
            for c in digitsToChar[digits[i]]:#it will combine each letter of string to the other string by backtracking till we get the len(curstr)==len(digits) condition
                backtrack(i+1,curstr+c)
        if digits:
            backtrack(0,"")
        return res
