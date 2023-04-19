class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack=[]
        stack.append(words[0])
        for i in range(1,len(words)):
            if sorted(stack[-1])!=sorted(words[i]):
                stack.append(words[i])
        return stack
''' Time Complexity--O(N*nlogn)
    Space Complexity--O(N)'''
