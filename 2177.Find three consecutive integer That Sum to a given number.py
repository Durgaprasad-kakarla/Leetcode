def sumOfThree(self, num: int) -> List[int]:
    nums=[]
    #if three numbers sum should be equal to the target number then that number should be divisible by 3.
    if num%3==0:
        #the number which is divisible by the the 3 and before and after of that number's sum will be equal to the target
        nums.append(num//3-1)
        nums.append(num//3)
        nums.append(num//3+1)
        return nums
