class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        list1=[]
        for i in tokens:
            if i.isdigit() or (len(i)>1 and i[0]=='-'):#if it is digit then append the element in the list1
                list1.append(i)
            else:#if i is not digit then evaluate the top two elements
                x=list1.pop()#delete the top two elements and store it in x and y.
                y=list1.pop()
                list1.append(math.trunc(eval(str(y)+str(i)+str(x))))#evaluate the two elements and append the evaluate element in the list1
        return int(list1[0])
