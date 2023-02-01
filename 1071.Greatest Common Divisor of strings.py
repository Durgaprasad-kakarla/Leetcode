class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str2)):
            for j in range(len(str2),-1,-1):
                if len(str2[i:j])!=0:
                    x=len(str1)//len(str2[i:j])
                    y=len(str2)//len(str2[i:j])
                    if len(str1)%len(str2[i:j])==0 and len(str2)%len(str2[i:j])==0 :
                        if str2[i:j]*x==(str1) and str2[i:j]*y==str2:
                            return str2[i:j]
        return ""
        
