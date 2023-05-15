class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permute(ip,op,list1):
            if len(ip)==0:
                list1.add(op)
                return
            ch=ip[0].lower()
            ch2=ip[0].upper()
            ip=ip[1:]
            permute(ip,op+ch,list1)
            permute(ip,op+ch2,list1)
        list1=set()
        permute(s,"",list1)
        return list1
''' Time Complexity--O(2^k*n)
    Space Complexity--O(n)'''
