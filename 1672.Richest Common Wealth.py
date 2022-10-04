class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max1=sum(accounts[0])
        for list1 in accounts:
            if sum(list1)>max1:
                max1=sum(list1)
        return max1
