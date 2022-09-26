class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dict1={'++X':1,'X++':1,'--X':-1,'X--':-1}
        sum1=0
        for i in operations:
            sum1+=dict1[i]
        return sum1
