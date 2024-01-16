import random
class RandomizedSet:

    def __init__(self):
        self.dic={}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val]=1
        return True

    def remove(self, val: int) -> bool:
        if val in self.dic:
            del self.dic[val]
            return True
        return False

    def getRandom(self) -> int:
        ele=random.randint(0,len(self.dic)-1)
        lst=list(self.dic.keys())
        return lst[ele]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
''' Time Complexity--O(1)
    Space Complexity--O(n)--inserted values into the dictionary'''
