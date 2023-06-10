class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sumOfNumbers(i,j):
            return (j*(j+1)//2) - ((i-1)*(i)//2)

        def check(num):
            totalSum = 0
            if index >= num:
                totalSum += index-num + 1
                i = 1
            else:
                i = num - index
            totalSum += sumOfNumbers(i,num)

            if n - index >= num:
                j = 1
                totalSum += n-index-num
            else:
                j = num - (n-index) + 1
            totalSum += sumOfNumbers(j,num-1)

            if totalSum<=maxSum:
                return True
            else:
                return False

        low = 1
        high = maxSum

        while(low<=high):
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1

        return low - 1
            
    ''' Time Complexity--O(logn)
        Space Complexity--O(1)
