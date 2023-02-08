class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==1:
            return True
        def binary_search(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0

            while low <= high:
                mid = (high + low) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        list1=[i*i for i in range(int(math.sqrt(c))+1) if i*i<=c]
        for i in range(len(list1)):
            if binary_search(list1,c-list1[i])!=-1:
                return True
        return False
